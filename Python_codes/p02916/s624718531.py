N = int(input())
A = [-1]
A.extend(list(map(int, input().split()))) # たべた料理
B = [-1]
B.extend(list(map(int, input().split()))) # 料理の満足度
C = [-1]
C.extend(list(map(int, input().split()))) # i -> i+1ボーナス

manzoku = 0

for i in range(1, N+1):
    manzoku += B[A[i]]
    if A[i-1] + 1 == A[i]:
        manzoku += C[A[i-1]]

print(manzoku)
