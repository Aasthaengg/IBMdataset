n=int(input())
a=[1]
b=2
s=1
def pr(x):
  for i in range(len(x)):
    print(x[i])
while s<=n:
  a.append(b)
  s+=b
  b+=1
if s==n:
  pr(a)
else:
  c=s-n
  a.remove(c)
  pr(a)