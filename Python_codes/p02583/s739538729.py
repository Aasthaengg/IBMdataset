from collections import defaultdict

n = int(input())
l_list = [int(x) for x in input().split()]

d = defaultdict(int)
for l in l_list:
    d[l] += 1

n = len(d)
l_list = sorted(d.keys())
ans = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            a, b, c = l_list[i], l_list[j], l_list[k]
            if a + b <= c:
                continue
            ans += d[a] * d[b] * d[c]
print(ans)