import bisect
N,M=map(int,input().split())
A=list(map(int,input().split()))
dic={}
s=0
for i in range(N):
  s+=A[i]
  r=s%M
  if r in dic.keys():
    dic[r].append(i)
  else:
    dic[r]=[i]
ans=0
s=0
for i in range(N):
  s+=A[i]
  r=s%M
  num=bisect.bisect_right(dic[r],i)
  ans+=(len(dic[r])-num)
  if r==0:ans+=1
print(ans)