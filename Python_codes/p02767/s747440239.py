def solve():
    N = int(input())
    X = [int(i) for i in input().split()]
    from decimal import Decimal, ROUND_HALF_UP
    target = int(Decimal(sum(X)/float(N)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
    ans = 0
    for x in X:
        ans += (x-target)**2
    print(ans)

if __name__ == "__main__":
    solve()