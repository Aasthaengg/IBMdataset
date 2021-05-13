n = int(input())
a = list(map(int,input().split()))

s = sum(a)
s1 = 0
for i in range(1,n,2):
    s1 += a[i]

ans = [s-s1*2]
for i in range(1,n):
    ans.append((a[i-1]-ans[i-1]//2)*2)

print(*ans)
