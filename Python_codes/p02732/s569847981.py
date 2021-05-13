n=int(input())
a=list(map(int,input().split()))
import collections
c=collections.Counter(a)
s=0
for cc in c:
  s+=c[cc]*(c[cc]-1)//2
for aa in a:
  sa=c[aa]*(c[aa]-1)//2-(c[aa]-1)*(c[aa]-2)//2
  print(s-sa)
