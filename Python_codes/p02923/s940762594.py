n = int(input())
h = list(map(int, input().split()))
max_val = 0
count = 0
for i in range(n-1):
    if h[i] >= h[i+1]:
        count += 1
    else:
        max_val = max(max_val, count)
        count = 0
max_val = max(max_val, count)
print(max_val)