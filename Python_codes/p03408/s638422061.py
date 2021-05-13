from collections import Counter

def solve():
    N = int(input())
    S = [input() for _ in range(N)]
    M = int(input())
    T = [input() for _ in range(M)]
    SC = Counter(S)
    TC = Counter(T)
    ans = 0
    for k, v in SC.items():
        ans = max(ans, v - TC.get(k, 0))
    print(ans)

if __name__ == "__main__":
    solve()
