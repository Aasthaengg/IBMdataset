n = int(input())
l = list(map(int, input().split()))
s = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j, n):
            if (l[i] == l[j]) | (l[j] == l[k]) | (l[i] == l[k]):
                continue
            if l[i] + l[j] <= l[k]:
                continue
            if abs(l[i]- l[j]) >= l[k]:
                continue
            s += 1
print(s)