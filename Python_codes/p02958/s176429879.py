s = 0
N = int(input())
H = list(map(int,input().split()))
K = list(range(1,N+1))

for i in range(N):
    if H[i]!=K[i]:
        s+=1
if s==0 or s==2:
    print("YES")
else:
    print("NO")