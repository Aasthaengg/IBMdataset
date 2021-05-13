import sys
def input(): return sys.stdin.readline().strip()


def main():
    N = int(input())
    S = input()
    ans = 0
    for n in range(N):
        S1 = set(S[:n])
        S2 = set(S[n:])
        I = S1 & S2
        ans = max(ans, len(I))
    print(ans)



if __name__ == "__main__":
    main()
