from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

n=int(input())
h=lnii()+[10**10]

ans=0
t_ans=0
for i in range(n):
  if h[i]>=h[i+1]:
    t_ans+=1
  else:
    ans=max(ans,t_ans)
    t_ans=0

print(ans)