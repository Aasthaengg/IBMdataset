n, m = input().split(" ")
n = int(n)
m = int(m)
k = []
for i in range(n):
    k.append([])
    tmp = input().split(" ")
    for j in range(1, len(tmp)):
        k[i].append(int(tmp[j]))

dict = {}
for i in range(1, m+1):
    dict[i] = 0

for i in k:
    for j in i:
        dict[j] += 1

cnt = 0
for i in range(1, m+1):
    if dict[i] == n:
        cnt += 1

print(cnt)

