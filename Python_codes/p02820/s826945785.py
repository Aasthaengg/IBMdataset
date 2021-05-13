n,k = map(int,input().split())
r,s,p = map(int,input().split())
t = input()
ans = 0
vstd = [0]*n
def jungkeng(x):
  global ans
  if x=='r':
    ans += p
  elif x=='s':
    ans += r
  else:
    ans += s
  return ans
  
for i in range(k):
  ans = jungkeng(t[i])
  vstd[i]=1
for i in range(k,n):
  if t[i]==t[i-k] and vstd[i-k]:
    continue
  ans = jungkeng(t[i])
  vstd[i] = 1
print(ans)