def solve():
    n = int(input())
    k = int(input())
    x = list(map(int, input().split()))
    ans = 0
    for i in x:
        cost = min(i*2, abs(k-i)*2)
        ans += cost
    print(ans)
    return 0

if __name__ == "__main__":
    solve()