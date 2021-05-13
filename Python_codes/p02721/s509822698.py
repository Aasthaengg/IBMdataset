n,k,c= map(int,input().split())
s = input()
i = 0

def func(s,k,c):
  i = 0
  res = []
  while 1:
    if s[i] == 'o':
      res.append(i)
      if len(res)== k:
        break
      i += c
    i+= 1
  return res
ans1 = func(s,k,c)
ans2 = func(s[::-1],k,c)
ans2 = [n-a-1 for a in ans2]
ans2 = ans2[::-1]

for i in range(k):
  if ans1[i]==ans2[i]:
    print(ans1[i]+1)


