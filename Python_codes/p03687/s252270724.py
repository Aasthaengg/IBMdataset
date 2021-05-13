def solve():
    S = input()
    ans = float('inf')

    for ch in set(S):
        dist = list(map(lambda x: len(x), S.split(ch)))
        ans = min(max(dist),ans)

    print(ans)

if __name__ == '__main__':
    solve()