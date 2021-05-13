n = int(input())
a = list(map(int,input().split()))
s = sum(a)
l1 = 0

for i in range(n):
    l1 += a[i] 
    if l1> s//2:break
r1 = s - l1
l2 = l1 -a[i]
r2 = s - l2
ans = min(abs(r1-l1),abs(r2-l2))
print(ans)