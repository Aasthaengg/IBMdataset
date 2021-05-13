from datetime import datetime as dt
import heapq
X,Y,Z,K = list(map(int,input().split(" ")))
As = list(map(int,input().split(" ")))
As.sort(reverse=True)
Bs = list(map(int,input().split(" ")))
Bs.sort(reverse=True)
Cs = list(map(int,input().split(" ")))
Cs.sort(reverse=True)

a = 0
b = 0
c = 0
se = set()
nums = []
num = As[a] + Bs[b] + Cs[c]
heapq.heappush(nums,(-num,(a ,b,c)))
# se.add((a ,b,c))
for _ in range(K):
    while True:
        temp = heapq.heappop(nums)
        num = temp[0]
        a,b,c = temp[1]
        if temp[1] in se:
            pass
        else:
            se.add(temp[1])
            break
    print(-num)
    #次のステップ
    if a + 1 < X:
        num = As[a + 1] + Bs[b] + Cs[c]
        heapq.heappush(nums,(-num,(a + 1,b,c)))
    if b + 1 < Y:
        num = As[a ] + Bs[b + 1] + Cs[c]
        heapq.heappush(nums,(-num,(a ,b + 1,c)))
    if c + 1 < Z:
        num = As[a] + Bs[b ] + Cs[c + 1]
        heapq.heappush(nums,(-num,(a ,b,c + 1)))


