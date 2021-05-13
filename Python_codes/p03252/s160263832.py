import sys
def input(): return sys.stdin.readline().strip()


def main():
    S = input()
    T = input()
    """
    置換が互換の積でかけることから、S->Tの変換がアルファベットの置換で表現できればよい。
    """
    d = {chr(i + 97): -1 for i in range(26)}
    d_inv = {chr(i + 97): -1 for i in range(26)}
    for i, s in enumerate(S):
        t = T[i]
        if d[s] != -1 or d_inv[t] != -1:
            if d[s] != t or d_inv[t] !=s:
                print("No")
                return
        d[s] = t
        d_inv[t] = s
    print("Yes")


if __name__ == "__main__":
    main()
