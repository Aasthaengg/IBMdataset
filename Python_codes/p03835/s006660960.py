a = input()
k, s = a.split(' ')
K = int(k)
S = int(s)
ans = 0
for x in range(K + 1):
    for y in range(K + 1):
        z = S - x - y
        if (z >= 0) and (z <= K):
            ans += 1

print(ans)