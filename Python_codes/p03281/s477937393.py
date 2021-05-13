import itertools
N = int(input())
S = [3,5,7,11,13]

if N >= 189:
  ans = 2
elif N>= 135:
  ans = 1
else:
  ans = 0
A = list(itertools.combinations(S,3))
#print(A)
for x in A:
  a,b,c = x
  if a*b*c <= N:
    ans += 1
print(ans)