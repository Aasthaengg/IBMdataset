N=int(input())
T,A=map(int,input().split())
h=list(map(int,input().split()))

t = (T-A)/0.006

MIN=10**9
argmin=-1
for i in range(N):
  diff = abs(h[i]-t)
  if diff<MIN:
    MIN=diff
    argmin=i

print(argmin+1)