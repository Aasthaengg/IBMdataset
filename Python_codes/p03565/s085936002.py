import sys
def input(): return sys.stdin.readline().strip()

def main():
    S = input()
    T = input()
    s = len(S)
    t = len(T)
    if s < t:
        print("UNRESTORABLE")
        return
    for i in range(s - t, -1, -1):
        correspond = True
        for j in range(t):
            if S[i + j] != '?' and S[i + j] != T[j]:
                correspond = False
                break
        if correspond:
            ans = [S[k] for k in range(s)]
            for j in range(t): ans[i + j] = T[j]
            for k in range(s):
                if ans[k] == '?': ans[k] = 'a'
            print("".join(ans))
            return
    print("UNRESTORABLE")

if __name__ == "__main__":
    main()
