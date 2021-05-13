import sys
def f(x):
  if x%2==0:
    return x//2
  else:
    return (x*3)+1
s=int(input())
S=list()
i=2
S.append(s)
while True:
  s=f(s)
  if s not in S:
    S.append(s)
  else:
    print(i)
    sys.exit()
  i+=1