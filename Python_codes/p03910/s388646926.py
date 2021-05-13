n = int(input())
r = 10**7+1
l = 1

def f(n):
  return (n**2+n)//2

while r-l> 1:
  if f((l+r)//2)>n:
    r = (l+r)//2
  else:
    l = (l+r)//2

l = l+1
rm = (l+1)*l//2-n
ans = list(range(1, l+1))
ans.remove(rm)
for a in ans:
  print(a)

