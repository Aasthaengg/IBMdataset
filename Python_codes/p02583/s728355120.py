n = int(input())
l = sorted(map(int, input().split()))
c = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if l[i] != l[j] != l[k] and l[i] + l[j] > l[k]:
                c += 1
print(c)