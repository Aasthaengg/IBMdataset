def solve():
    ans = 0
    N = int(input())
    for i in range(N):
        x,y = map(int, input().split())
        ans += y-x+1
    return ans
print(solve())