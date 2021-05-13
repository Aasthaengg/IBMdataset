n = int(input())
s = input()


ans = []
for i in range(1, n):
  a = s[0:i]
  b = s[i:n]
  res = []
  for j in a:
    if j in b and j not in res:
      res.append(j)
    ans.append(len(res))
    
print(max(ans))