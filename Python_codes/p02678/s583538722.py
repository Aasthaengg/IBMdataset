import queue

N, M = map(int, input().split())
root = [[] for i in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    root[A-1].append(B-1)
    root[B-1].append(A-1)

#sign:道しるべがどこを示しているか
sign = [-1]*N
sign[0] = 0

flag = True

# FIFOキューの作成
q = queue.Queue()
q.put(0)
r = queue.Queue()


while flag:
    flag = False
    num = 1

    while not q.empty():
        hoge = q.get()
        for i in range(len(root[hoge])):
            if sign[root[hoge][i]] == -1:
                sign[root[hoge][i]] = hoge
                r.put(root[hoge][i])
                flag = True

    while not r.empty():
        q.put(r.get())

    num += 1

if sign.count(-1) == 0:
    print("Yes")
    for i in range(1,N):
        print(sign[i]+1)
else:
    print("No")
    print(sign)