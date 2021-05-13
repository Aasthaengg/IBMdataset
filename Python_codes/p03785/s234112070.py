import sys
n,c,k,*t = map(int, sys.stdin.read().split())
t.sort()

i=0
cnt=0
while i<n:
  departure=t[i]+k
  p=0
  for j in range(i,n):
    if t[j] > departure or p==c:
      break
    p+=1
  i+=p
  cnt+=1
print(cnt)

