from collections import*
h,w,n=map(int,input().split())
d=defaultdict(int)
for x in[0]*n:
  a,b=map(int,input().split())
  for i in[a-1,a,a+1]:
    for j in[b-1,b,b+1]:d[(i,j)]+=1
c=[0]*10;c[0]=(w-2)*(h-2)
for i in d:
  a,b=i
  if 1<a<h and 1<b<w:c[d[i]]+=1;c[0]-=1
for i in c:print(i)