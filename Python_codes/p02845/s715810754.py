N = int(input())
A = list(map(int, input().split()))
C = [0, 0, 0]  # 同じ帽子をかぶっている人数　降順
B = 10 ** 9 + 7
ans = 1
for i in range(N):
    if A[i] in C:
        ans *= C.count(A[i])
        C[C.index(A[i])] += 1
    else:
        ans = 0
        break
print(ans % B)
