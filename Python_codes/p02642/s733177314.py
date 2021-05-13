n=int(input())
A=sorted(list(map(int,input().split())))
B=[0]*(1+A[-1])
for i in A:
    B[i]+=1
    if B[i]==1:
        for j in range(2*i,A[-1]+1,i):
            B[j]+=1
    else:
        continue
ans=0
for i in A:
  if B[i]==1: ans+=1

print(ans)