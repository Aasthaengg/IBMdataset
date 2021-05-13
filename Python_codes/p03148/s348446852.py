import heapq

N, K = map(int, input().split())
sushi = []

for _ in range(N):
    t, d = map(int, input().split())
    sushi.append((t, d))
sushi = sorted(sushi, key=lambda x: -x[1])

d_sushi = []  # 捨てる候補の寿司
heapq.heapify(d_sushi)  # リストaのheap化

fp = 0
tp = set()

for i in range(K):
    fp += sushi[i][1]
    if sushi[i][0] in tp:
        heapq.heappush(d_sushi, sushi[i][1])
    else:
        tp.add(sushi[i][0])
ans = fp+len(tp)**2

if N == K:
    print(ans)
    exit()

j = K
while d_sushi and len(tp) <= N:
    while sushi[j][0] in tp:
        j += 1
        if j == N:
            print(ans)
            exit()
    fp = fp-heapq.heappop(d_sushi)+sushi[j][1]
    tp.add(sushi[j][0])
    ans = max(ans, fp+len(tp)**2)

print(ans)
