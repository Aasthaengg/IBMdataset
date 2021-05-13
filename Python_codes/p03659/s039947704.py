n = int(input())
a = list(map(int,input().split()))
l = [0]*n
l[0] = a[0]

for i in range(1,n):
    l[i] = l[i-1] + a[i]
sum = sum(a)
ans = 10**10+1
for i in range(len(l)-1):
    x = l[i]
    y = sum - l[i]
    tmp = abs(x-y)
    ans = min(ans,tmp)

print(ans)
