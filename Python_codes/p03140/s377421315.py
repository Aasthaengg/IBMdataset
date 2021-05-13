# 全国統一プログラミング王決定戦予選/NIKKEI Programming Contest 2019: B – Touitsu
N = int(input())
A, B, C = [input() for _ in range(3)]

operations = 0

for i in range(N):
    if A[i] == B[i] == C[i]:
        pass
    elif A[i] == B[i] or B[i] == C[i] or C[i] == A[i]:
        operations += 1
    else:
        operations += 2

print(operations)