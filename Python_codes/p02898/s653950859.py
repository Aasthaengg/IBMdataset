n,k = map(int, input().split())
h = list(map(int, input().split()))
cnt = 0
for i in range(len(h)):
    if h[i]>=k:
        cnt += 1
    else:
        continue
print(cnt)