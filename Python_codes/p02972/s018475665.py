N = int(input())
alist = list(map(int, input().split()))

box = [0] * (N + 1)

for i in range(N, 0, -1):
    cnt = 0
    for j in range(i*2, N+1, i):
        cnt += box[j]
    if cnt%2 != alist[i-1]:
        box[i] = 1

M = sum(box)
ans = []
for i in range(1, N+1):
    if box[i]:
        ans.append("{}".format(i))

print(M)
print(" ".join(ans))