##C - Step(TLE)
N = int(input())
A = list(map(int,input().split()))
ans = 0
maxi = 0
for i in A:
    ans += max(0,maxi-i)
    maxi = max(maxi,i)
print(ans)