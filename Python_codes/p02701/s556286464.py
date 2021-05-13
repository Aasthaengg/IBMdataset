n = int(input())
d = {}
ans = 0
for i in range(n):
  s = input()
  if d.get(s, 0)==0:
    d[s]=1
    ans+=1
print(ans)