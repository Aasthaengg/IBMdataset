import collections
import heapq
x,y,z,k = map(int,(input().split()))
a = list(map(int,(input().split())))
b = list(map(int,(input().split())))
c = list(map(int,(input().split())))
a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)
big = [(-a[0]-b[0]-c[0],0,0,0)]
heapq.heapify(big)

visited = collections.defaultdict(int)

ans = []
C = 0
while C < k:
    if big[0][1]+1 < len(a) and not visited[(big[0][1]+1,big[0][2],big[0][3])]:
        heapq.heappush(big, (-a[big[0][1]+1]-b[big[0][2]]-c[big[0][3]],big[0][1]+1,big[0][2],big[0][3] ) )
        visited[(big[0][1]+1,big[0][2],big[0][3])] = 1
    if big[0][2]+1 < len(b) and not visited[(big[0][1],big[0][2]+1,big[0][3])]:
        heapq.heappush(big, (-a[big[0][1]]-b[big[0][2]+1]-c[big[0][3]],big[0][1],big[0][2]+1,big[0][3] ) )
        visited[(big[0][1],big[0][2]+1,big[0][3])] = 1
    if big[0][3]+1 < len(c) and not visited[(big[0][1],big[0][2],big[0][3]+1)]:
        heapq.heappush(big, (-a[big[0][1]]-b[big[0][2]]-c[big[0][3]+1],big[0][1],big[0][2],big[0][3]+1 ) )
        visited[(big[0][1],big[0][2],big[0][3]+1)] = 1
    ans.append(heapq.heappop(big))
    C += 1

for i in ans:
    print(-i[0])