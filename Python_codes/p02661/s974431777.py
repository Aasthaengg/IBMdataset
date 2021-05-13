n=int(input())
alis=[]
blis=[]
for i in range(n):
  a,b=map(int,input().split())
  alis.append(a)
  blis.append(b)
  
  
alis=sorted(alis)
blis=sorted(blis)
if n%2!=0:
  print(blis[int((n-1)/2)]-alis[int((n-1)/2)]+1)
else:
  bb=(blis[int(n/2)-1]+blis[int(n/2)])
  aa=(alis[int(n/2)-1]+alis[int(n/2)])
  print(bb-aa+1)