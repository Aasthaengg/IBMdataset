N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
BC = [list(map(int, input().split())) for i in range(M)]

# Cについて大きい順にソート
BC.sort(key=lambda x: x[1], reverse=True)

temp = []
for i in range(M):
        # CiをBi個追加
    temp += [BC[i][1]] * BC[i][0]
    if len(temp) > N:
        break

A += temp
A.sort(reverse=True)

print(sum(A[:N]))
