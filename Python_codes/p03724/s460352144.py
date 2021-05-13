N,M=map(int,input().split())

B=[0]*N

for i in range(M):
    a,b=map(int,input().split())
    B[a-1]+=1
    B[b-1]+=1

for i in range(N):
    if B[i]%2==1:
        print("NO")
        exit()
print("YES")