N = int(input())
p = list(map(int, input().split()))

res = 0
for i in range(len(p) - 1):
    if i + 1 != p[i]:
        continue

    res += 1
    tmp = p[i]
    p[i] = p[i+1]
    p[i+1] = tmp

if N == p[N-1]:
    res += 1

print(res)
