n, k = [int(x) for x in input().split()]
h = [int(x) for x in input().split()]
cnt = 0
for i in range(len(h)):
    if h[i] >= k:
        cnt += 1
print(cnt)
