n,m = map(int,input().split())
A = list(map(int,input().split()))
tehuda = []
for i in range(m):
    b,c = map(int,input().split())
    tehuda.append((b,c))
# とりあえず和
sumA = sum(A)
import heapq
heapq.heapify(A)
tehuda = sorted(tehuda,key = lambda x:x[1])
#print(tehuda)
over = True
while tehuda:
    if not over:
        break
    b,c = tehuda.pop()
    while True:
        m = heapq.heappop(A)
        #print(m,c)
        if m >= c:
            over = False
            break
        else:
            b -= 1
            sumA -= m
            sumA += c
            heapq.heappush(A,c)
            if b == 0:
                break
print(sumA)
