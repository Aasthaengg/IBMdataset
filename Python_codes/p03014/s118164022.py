from itertools import chain
H, W = map(int, input().split())
S = [input()+"#" for _ in range(H)]
S.append("#"*(W+1))
A = [[0]*(W) for _ in range(H)]

for i in range(H):
    tmp = 0
    stack = []
    for j in range(W+1):
        if S[i][j] == ".":
            tmp += 1
            stack.append(j)
        # elif j == W-1:
        #     if S[i][j] == ".":
        #         tmp += 1
        #         stack.append(j)
            
        #     while stack:
        #         tmp_j = stack.pop()
        #         A[i][tmp_j] += tmp
        #     tmp = 0
        else:
            while stack:
                tmp_j = stack.pop()
                A[i][tmp_j] += tmp
            tmp = 0
for j in range(W):
    tmp = 0
    stack = []
    for i in range(H+1):
        if S[i][j] == ".":
            tmp += 1
            stack.append(i)
        # elif i == H-1:
        #     if S[i][j] == ".":
        #         tmp += 1
        #         stack.append(i)
        #     while stack:
        #         tmp_i = stack.pop()
        #         A[tmp_i][j] += tmp
        #     tmp = 0
        else:
            while stack:
                tmp_i = stack.pop()
                A[tmp_i][j] += tmp
            tmp = 0
ans = max(chain.from_iterable(A))-1
print(ans)