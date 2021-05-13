n = int(input())
l = []
r = []

for i in range(n):
    a,b = map(int,input().split())
    l.append(a)
    r.append(b)
    
ans = 0
for i in range(n):
    ans +=r[i] - l[i] + 1
    
print(ans)