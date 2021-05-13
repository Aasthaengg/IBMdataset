import heapq
n = int(input())
heap_a = list(map(int, input().split()))

# N＝５０だと、多くても４９
# > 愚直にやっても大丈夫なはず。なるべく早く実行するために、Heapqを使用する。

heapq.heapify(heap_a)

#tar = heapq.nsmallest(2, heap_a)
while True:
    tar1 = heapq.heappop(heap_a)
    tar2 = heapq.heappop(heap_a)

    heapq.heappush(heap_a, (tar1 + tar2) / 2.0)
    if (len(heap_a) == 1):
        break


print(heapq.heappop(heap_a))
