n = int(input())
p = list(map(int, input().split()))
a = 0
for i in range(len(p) - 2):
    if p[i] < p[i + 1] < p[i + 2] or p[i + 2] < p[i + 1] < p[i]:
        a += 1
print(a)