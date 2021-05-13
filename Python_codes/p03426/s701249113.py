h,w,d=map(int,input().split())
a=[ [ [] for j in range(int(h*w/d+1)) ] for i in range(d) ]
a1=[ [ [] for j in range(int(h*w/d+1)) ] for i in range(d) ]
for i in range(h):
  i+=1
  tmp=list(map(int,input().split()))
  for j in range(w):
    num=tmp[j]
    j+=1
    a[num%d][int( (num-1)/d)]=[i,j]
for i in range(len(a)):
  a1[i][0]=0
  for j in range(len(a[i])-1):
    j=j+1
    if a[i][j]!=[]:
      a1[i][j]=a1[i][j-1]+abs(a[i][j][0]-a[i][j-1][0])+abs(a[i][j][1]-a[i][j-1][1])

q=int(input())
for i in range(q):
  l,r=map(int,input().split())
  print(a1[l%d][int((r-1)/d)]-a1[l%d][int((l-1)/d)])
