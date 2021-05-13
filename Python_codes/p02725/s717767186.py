K, N = map(int, input().split())
A = list(map(int, input().split()))
max_dis = 0
max_i = 0
for i in range(N):
    if i==0:
        max_dis = A[0] + (K - A[-1])
        max_i = 0
    else:
        dis = A[i]-A[i-1]
        if max_dis < dis:
            max_dis = dis
            max_i = i
if max_i == 0:
    move_dis = A[-1] - A[0]
    print(move_dis)
else:
    move_dis = (K-A[max_i]) + A[max_i-1]
    print(move_dis)