n,c,k = tuple(map(int,input().split()))
t = []

for i in range(n):
  t.append(int(input()))
t = sorted(t)
t_0 = t[0]
p = 1
ans = 0
for t_i in t[1:]:
  if p<c and t_i-t_0<=k:
    p+=1
  else:
    p = 1
    t_0 = t_i
    ans+=1
    
print(ans+1)