n = int(input())
p = list(map(int, input().split()))

count = 0
for i in range(1, len(p)-1):
    p_min = max(p[i-1], p[i], p[i+1])
    p_max = min(p[i-1], p[i], p[i+1])
    if p_min != p[i] and p_max != p[i]:
        count += 1
print(count)
