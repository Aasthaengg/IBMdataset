n = int(input())
p = tuple(map(int,input().split()))

ans = 0
m = p[0]
for i in range(n):
  if m >= p[i]:
    ans+=1
    m = p[i]
print(ans)  
