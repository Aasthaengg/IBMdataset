n=int(input())

t = list(map(int,input().split()))

t.sort()

ans = 0

for i in range(1,n):
    ans += t[i]-t[i-1]
print(ans)
