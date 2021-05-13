import queue

N = int(input())
K = int(input())

que = queue.Queue()
que.put((1, 0))

min = -1
while (True):
    if que.empty():
        break
    test = que.get()
    # print(test)
    num = test[0]
    count = test[1]
    if count == N:
        if min == -1 or min > test[0]:
            min = test[0]
        continue
    que.put((num * 2, count + 1))
    que.put((num + K, count + 1))
print(min)
