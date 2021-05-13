N=int(input())
P=list(map(int,input().split()))
Q=sorted(P)
count=0
for i in range(N):
    if P[i]!=Q[i]:
        count=count+1
    else:
        pass
if count==0 or count==2:
    print("YES")
else:
    print("NO")