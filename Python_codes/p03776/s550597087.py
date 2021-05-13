from math import factorial as fact
def comb(n, r):
  denom = fact(r)*fact(n-r)
  return fact(n)//denom

n = list(map(int, input().split()))
l = list(map(int, input().split()))

l = sorted(l)

summ = 0

for i in range(n[1]):
  summ+=l[len(l)-1-i]

avg = float(summ)/n[1]
last =  l[len(l)-n[1]]
lasts = l.count(last)
more = sum(1 for i in l if i>last)
print(avg)
if more!=0:
  answer = comb(lasts, n[1]-more)
  print(answer)
else:
  b= min(lasts, n[2])
  answer = 0
  for i in range(n[1], b+1):
    answer += comb(lasts, i)
  print(answer)