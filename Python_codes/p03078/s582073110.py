import heapq

x, y, z, k = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=True)
B = sorted(list(map(int, input().split())), reverse=True)
C = sorted(list(map(int, input().split())), reverse=True)

# A+B+Cが大きい順になるようにリストに入れていく
ABC = []

# heapqに任意の値が入っているか確認する
from collections import defaultdict
d = defaultdict(int)

que = []

def HeapPush(a, b, c):
    if d[(a, b, c)] == 0:
        heapq.heappush(que, ((A[a] + B[b] + C[c])*-1, a, b, c))  # -1を掛ける
        d[(a, b, c)] += 1


HeapPush(0, 0, 0)

while len(ABC) < k:
    
    abc, a, b, c = heapq.heappop(que)
    ABC.append(abc*-1)  # -1を掛け直す
    
    if a + 1 < x:
        HeapPush(a+1, b, c)
    if b + 1 < y:
        HeapPush(a, b+1, c)
    if c + 1 < z:
        HeapPush(a, b, c+1)
   

for abc in ABC:
    print(abc)