N,M=map(int,input().split())
L=[0 for i in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    L[a]+=1
    L[b]+=1

for i in range(1,len(L)):
    if L[i]%2==1:
        print("NO")
        exit()
print("YES")