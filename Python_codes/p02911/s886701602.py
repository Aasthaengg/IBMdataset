n,k,q=map(int, input().split())
score=[0]*(n+1)
for i in range(q):
    tmp=int(input())
    score[tmp]+=1

for i in range(1,len(score)):
    if k+score[i]-q>0:print("Yes")
    else:print("No")
