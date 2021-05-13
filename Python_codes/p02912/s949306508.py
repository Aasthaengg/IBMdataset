import heapq
N,M=map(int,input().split())
a=list(map(int,input().split()))
a = list(map(lambda x: x * (-1), a))  # 各要素を-1倍
heapq.heapify(a)  # リストを優先度付きキューへ
for _ in range(M):
    number=heapq.heappop(a)  # 最大値の取り出し
    if number%2==0:
        number=number//2
    else:
        number=number//2+1
    heapq.heappush(a, number)  # 要素の挿入
print(-sum(a))
