N=int(input())
L=[0 for i in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        if i*j<=N:
            L[i*j]+=1
cnt=0
for i in range(N+1):
    if i%2!=0 and L[i]==8:
        cnt+=1
print(cnt)
#print(L)