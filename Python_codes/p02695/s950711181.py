# 素朴に実装
N, M, Q = [int(i) for i in input().split()]
B = [[0, 0, 0, 0] for i in range(Q)]
for i in range(Q):
    B[i][0], B[i][1], B[i][2], B[i][3] = [int(j) for j in input().split()]
MAXC = [0]

def dfs(A, pre):
    # 終端条件 --- 10 重ループまで回したら処理して打ち切り
    if len(A) == N:
        counter = 0
        for i in range(Q):
            if A[B[i][1]-1] - A[B[i][0]-1] == B[i][2]:
                counter += B[i][3]
        if MAXC[0] < counter:
            MAXC[0] = counter
        return 
    for v in range(pre, M+1):
        A.append(v)
        dfs(A, v)
        A.pop() 
dfs([], 1)
print(MAXC[0])