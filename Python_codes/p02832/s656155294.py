from collections import deque
N = int(input())
Query = deque(map(int,input().split()))
ju = 1
Answer = 0
for i in range(N):
    q = Query.popleft()
    if q == ju:
        ju +=1
    else:
        Answer += 1
if ju == 1:
    Answer = -1
print(Answer)