N = int(input())
A = list(map(int,input().split()))
B = sorted(A)
ans1 = B[N // 2 - 1]
ans2 = B[N // 2]
for i in range(N):
    if A[i] > ans1:  print(ans1)
    else:  print(ans2)