N = int(input())
A = [int(input()) for _ in range(N)]
cnt = 0
for i in range(N):
    if A[i]%2==1:
        cnt += 1
if cnt>0:
    print("first")
else:
    print("second")