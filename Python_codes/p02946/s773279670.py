k,x = map(int, input().split())
s = x-k
e = x+k
ans = []


for i in range(s+1,e):
  i = str(i)
  ans.append(i)
  
print(' '. join(ans))