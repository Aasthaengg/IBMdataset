N = int(input())
A = [int(input()) for _ in range(N)]
flag = 0
for i in range(N):
    if A[i]%2==1:
        flag = 1
        break
if flag==1:
    print("first")
else:
    print("second")