N = int(input())
P = [int(input()) for _ in range(N)]
index = [-1] * N
for i, p in enumerate(P):
    index[p-1] = i
res = 1
tmp = 1
for i in range(N-1):
    if index[i] < index[i+1]:
        tmp += 1
        res = max(res, tmp)
    else:
        tmp = 1
ans = N-res
print(ans)