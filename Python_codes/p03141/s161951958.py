import heapq

N = int(input())
happiness = [list(map(int, input().split())) for i in range(N)]

queue = []
for i in range(N):
    x, y = happiness[i]
    queue.append([-(x+y), x, y])

heapq.heapify(queue)
takahashi = 0
aoki = 0
for i in range(N):
    dish = heapq.heappop(queue)
    if i % 2 == 0:
        takahashi += dish[1]
    else:
        aoki += dish[2]

print(takahashi-aoki)