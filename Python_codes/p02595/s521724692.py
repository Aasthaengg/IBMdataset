def solve():
    import math
    N,D = [int(i) for i in input().split()]
    ans = 0
    for i in range(N):
        x,y = [int(i) for i in input().split()]
        if math.sqrt(x**2+y**2) <= D:
            ans += 1
    print(ans)

if __name__ == "__main__":
    solve()