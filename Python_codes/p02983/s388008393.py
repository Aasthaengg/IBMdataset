
def solve():
    i = (L//2019) + 1
    ans = 0
    if L <= 2019*i <= R:
        print(ans)
    else:
        ans = 2020
        for n in range(L,R):
            for m in range(n+1,R+1):
                ans = min(ans, (n*m)%2019)
            if ans == 0:
                break
        print(ans)

if __name__ == "__main__":
    L,R = list(map(int, input().split()))
    solve()
