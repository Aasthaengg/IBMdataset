n = int(input())
p = list(map(int, input().split()))

p_sorted = sorted(p)
diff = 0
for i in range(n):
    if p[i] != p_sorted[i]:
        diff += 1
print('YES'if diff <= 2 else 'NO')
