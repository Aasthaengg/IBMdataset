N, M = map(int, input().split())
A = sorted(map(int, input().split()))
L = []
for _ in range(M):
    b, c = map(int, input().split())
    L.append([b, c])
L.sort(key=lambda x: x[1], reverse=True)
# 変更前のカードの枚数
# 変更後のカードの枚数
# をそれぞれ保存しておく

idx = 0
for i in range(N):
    if (idx > len(L) - 1):
        break
    if (A[i] < L[idx][1]):
        A[i] = L[idx][1]
        L[idx][0] -= 1
        if (L[idx][0] != 0):
            continue
        else:
            idx += 1
    else:
        break
print(sum(A))
