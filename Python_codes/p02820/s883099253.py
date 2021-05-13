n,k=map(int,input().split())
r,s,p=map(int,input().split())
t = input()
d = [0]*3*10**5
for i in range(n):
  if t[i] == 'r':
    d[i] = (10**4+1)+p
  if t[i] == 's':
    d[i] = 2*(10**4+1)+r
  if t[i] == 'p':
    d[i] = 3*(10**4+1)+s
ans = 0
for i in range(n):
  if d[i] == d[k+i]:
    d[k+i] = 0
  ans += d[i]%(10**4+1)
print(ans)