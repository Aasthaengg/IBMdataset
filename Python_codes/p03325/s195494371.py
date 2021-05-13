def solve():
    N = int(input())
    A = [int(i) for i in input().split()]
    ans = 0
    for a in A:
        while a % 2 == 0:
            ans += 1
            a //= 2
    print(ans)
    

if __name__ == "__main__":
    solve()
