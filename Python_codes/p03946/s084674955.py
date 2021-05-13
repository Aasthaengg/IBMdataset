n,t = map(int,input().split())
a = list(map(int,input().split()))
md = 0
c = 0
m = a[-1]
for i in range(2,n+1):
  if m-a[-i] > md:
    md = m-a[-i]
    c = 1
  elif m-a[-i] == md:
    c += 1
  m = max(m,a[-i])
print(c)