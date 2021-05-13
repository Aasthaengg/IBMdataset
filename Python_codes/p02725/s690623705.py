K,N = map(int, input().split())
li = list(map(int, input().split()))
max_len = 0
for i in range(N-1):
    if abs(li[i] - li[i+1]) > max_len:
        max_len = abs(li[i] - li[i+1])
if (K - max(li)) + min(li) > max_len:
    max_len = (K - max(li)) + min(li)
print(K - max_len)