import collections
h,w,n=map(int,input().split())
l=[list(map(int,input().split())) for i in range(n)]
L=[]
for i in range(n):
  for j in range(3):
    for k in range(3):
      if 0<l[i][0]-j<h-1 and 0<l[i][1]-k<w-1:
        L.append((l[i][0]-j-1)*10**9+l[i][1]-k-1)
L=collections.Counter(L)
L2=list(L.values())
ans=[0 for i in range(10)]
for i in range(len(L2)):
  ans[L2[i]]+=1
ans[0]=(h-2)*(w-2)-len(L2)
for i in range(10):
  print(ans[i])