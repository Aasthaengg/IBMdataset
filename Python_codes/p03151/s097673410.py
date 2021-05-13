from queue import Queue

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

D = [a - b for a, b in zip(A, B)]
Dm = [d for d in D if d < 0]
sum_Dm = abs(sum(Dm))

if sum_Dm == 0:
    print(0)
    exit(0)

Dp = [d for d in D if d > 0]
Dp.sort(reverse=True)

que = Queue()
for d in Dp:
    que.put(d)

cnt = 0
while not que.empty():
    p = que.get()
    cnt += 1
    sum_Dm -= p
    if sum_Dm <= 0:
        print(len(Dm) + cnt)
        exit(0)

print(-1)
