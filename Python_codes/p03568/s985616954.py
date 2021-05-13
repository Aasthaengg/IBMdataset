from collections import Counter as co 
n=int(input())
l=sorted(co([a%2 for a in map(int,input().split())]).most_common())
if len(l)==1:
  if l[0][0]==0:
    print(3**n-2**n)
  else:print(3**n-1)
else:
  g,k=l[0][1],l[1][1]
  print(3**n-2**g)