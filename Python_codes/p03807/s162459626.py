N = int(input())
A = list(map(int,input().split()))
cnt = 0
for i in range(N):
    if A[i]%2==1:
        cnt += 1
if cnt%2==0:
    print("YES")
else:
    print("NO")