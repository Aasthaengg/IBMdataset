s=int(input())
def f(x):
  if x%2==0:
    return x//2
  else:
    return 3*x+1
alist=[s]
for i in range(2,1000001):
  s=f(s)
  if s in alist:
    print(i)
    break
  else:
    alist.append(s)