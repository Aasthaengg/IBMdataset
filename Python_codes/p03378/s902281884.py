N,M,X=map(int,input().split())
A=list(map(int,input().split()))
ans1=0
ans2=0
for i in range(X):
    if i in A:
        ans1+=1

for j in range(X,N+1):
    if j in A:
        ans2+=1

if ans1<ans2:
    print(ans1)
else:
    print(ans2)