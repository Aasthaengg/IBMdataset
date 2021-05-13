N = int(input())
A = list(map(int, input().split()))
Q = int(input())
BC = [list(map(int, input().split())) for _ in range(Q)]

num = [0] * 100001
for a in A:
    num[a] += 1
S = sum(A)
for i in range(Q):
    S += (BC[i][1] - BC[i][0]) * num[BC[i][0]]
    print(S)
    num[BC[i][1]] += num[BC[i][0]]
    num[BC[i][0]] = 0
