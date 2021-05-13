N, A, B, C = map(int, input().split())
T = []
for i in range(N):
    T.append(int(input()))

ans = float("inf")
def loop(K):
    global ans
    abs_A = []
    abs_B = []
    abs_C = []
    for i in range(len(K)):
        abs_A.append(abs(A - K[i]))
        abs_B.append(abs(B - K[i]))
        abs_C.append(abs(C - K[i]))
    for i in range(len(K)):
        for j in range(len(K)):
            for k in range(len(K)):
                if i != j and j != k and k != i:
                    ans = min(ans, 10*(N-len(K)) + abs_A[i] + abs_B[j] + abs_C[k])
    if len(K) > 3:
        Next = []
        for i in range(len(K)):
            for j in range(i+1, len(K)):
                for p in range(len(K)):
                    if p != i and p != j:
                        Next.append(K[p])
                Next.append(K[i] + K[j])
                loop(Next)
                Next = []

loop(T)
print(ans)