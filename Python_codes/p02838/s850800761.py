import sys
input = sys.stdin.readline

N=int(input().rstrip('\n'))
A=[int(x) for x in input().rstrip('\n').split()]
res = 0
t=1
for _ in range(60):
  n = sum(x%2 for x in A)
  A = [x//2 for x in A]
  res += n*(N-n)*t
  t = t*2
  res = res%(7+10**9)
  if all(x==0 for x in A):
    break
print(res)