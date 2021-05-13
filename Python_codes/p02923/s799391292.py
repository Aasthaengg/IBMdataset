n = int(input())
h = list(map(int, input().split()))

max_ = 0
cnt = 0
for i in range(n - 1, 0, -1):
    if h[i - 1] < h[i]:
        max_ = max(max_, cnt)
        cnt = 0
    else:
        cnt += 1
max_ = max(max_, cnt)        
print(max_)