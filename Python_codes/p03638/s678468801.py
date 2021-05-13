h,w=map(int,input().split())
n=int(input())
a=list(map(int,input().split()))
l=[]
for i,j in enumerate(a):
  for _ in range(j):
    l.append(i+1)
for i in range(h):
  print(*l[i*w:(i+1)*w][::(-1)**i])