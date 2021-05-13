n=int(input())
R=[0 for _ in range(n)]
a=list(map(int,input().split()))
for i in range(n-1):
    R[a[i]-1]+=1

for z in range(n):
    print(R[z])
