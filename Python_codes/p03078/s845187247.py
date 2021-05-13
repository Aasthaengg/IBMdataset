import heapq
import sys
x, y, z, k = map(int, input().split())

a, b, c = (sorted(map(int, sys.stdin.readline().split()), reverse=True) for _ in range(3))

abc = {(0,0,0)}

stu = [[-a[0]-b[0]-c[0], 0,0,0]]
heapq.heapify(stu)
result = []
while k > 0:
    out_p, n, m, l = heapq.heappop(stu)
    if n+1<x and not((n+1,m,l) in abc):
        abc.add((n+1,m,l))
        heapq.heappush(stu, [-a[n+1]-b[m]-c[l], n+1, m, l])
    if m+1<y and not((n,m+1,l) in abc):
        abc.add((n,m+1,l))
        heapq.heappush(stu, [-a[n]-b[m+1]-c[l], n, m+1, l])
    if l+1<z and not((n,m,l+1) in abc):
        abc.add((n,m,l+1))
        heapq.heappush(stu, [-a[n]-b[m]-c[l+1], n, m, l+1])
    result.append(-out_p)
    k -= 1
result.sort(reverse=True)
for i in result:
    print(i)