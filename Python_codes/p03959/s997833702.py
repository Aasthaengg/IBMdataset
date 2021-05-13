n = int(input())
t = list(map(int, input().split(' ')))
a = list(map(int, input().split(' ')))
result = 1
for i in range(n):
    h_max, h_min = min(t[i], a[i])+1, 1
    if i != 0:
        if t[i-1] < t[i]:
            h_min = t[i]
    else:
        h_min = t[0]

    if i != n-1:
        if a[i] > a[i+1]:
            h_min = max(a[i], h_min)
    else:
        h_min = max(a[i], h_min)
    result = result * max(h_max - h_min, 0) % (10**9+7)
print(result)