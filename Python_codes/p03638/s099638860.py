h,w=map(int,input().split())
n=int(input())
A=list(map(int,input().split()))

out=[]
for i,a in enumerate(A):
  for _ in range(a):
    out.append(i+1)
ans,cnt=[],0
for i in range(h):
  if i%2==0:
    ans.append([out[cnt+j] for j in range(w)])
  else:
    ans.append([out[cnt+w-1-j] for j in range(w)])
  cnt+=w
for a in ans:
  print(*a)