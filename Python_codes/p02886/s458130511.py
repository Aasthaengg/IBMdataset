n = int(input())
d = list(map(int, input().split()))
s = 0

for i in range(n):
    for j in range(n):
        if i != j:
            s += d[i]*d[j]

s //= 2

print(s)
