N, K = map(int, input().split())
l = [0 for i in range(100001)]
num_count = 0
n = 0
for j in range(N):
    a, b = map(int, input().split())
    l[a] += b
for k in l:
    num_count += k
    if num_count >= K:
        print(n)
        break
    else:
        n += 1