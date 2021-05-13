n, k = map(int, input().split())
h = list(map(int,input().split()))
ans = []
for i in range(len(h)):
    if h[i] >= k:
        ans.append(h[i])

print(len(ans))
