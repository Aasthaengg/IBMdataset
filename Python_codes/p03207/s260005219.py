n = int(input())
l = []
temp = -1
idx = -1
for i in range(n):
    l.append(int(input()))
    if temp < l[i]:
        temp = l[i]
        idx = i
print(sum(l[:idx]) + l[idx] // 2 + sum(l[idx + 1:]))
