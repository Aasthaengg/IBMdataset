import itertools as it

N = list(input())
l = len(N)
a = N[0]+"9"*(l-1) #N[0]+9...9

ans = int(N[0])+9*(l-1)

if int("".join(N))!=int(a):
  ans-=1

print(ans)