N = int(input())
A = [int(input()) for _ in range(N)]
flag = False
for i in range(N):
    if A[i] % 2 == 1:
        flag = True

if flag:
    print("first")
else:
    print("second")
