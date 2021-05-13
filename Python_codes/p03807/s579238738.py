N = int(input())
A = list(map(int, input().split()))
g=0
k=0
for i in range(N):
    if A[i]%2==0:
        g+=1
    else:
        k+=1
if k%2==0:
    print("YES")
else:
    print("NO")