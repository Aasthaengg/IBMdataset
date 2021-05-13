N, K = map(int,input().split())
A = list(map(int,input().split()))
A.insert(0,0)
list = []
replist = []
judge = [True] * (2 * 10 ** 5 + 1)
pos = 1
owari = True
while owari:
    judge[pos] = False
    list.append(pos)
    pos = A[pos]
    if not judge[pos]:
        while True:
            replist.append(pos)
            judge[pos] = True
            pos = A[pos]
            if judge[pos]:
                owari = False
                break
if K <= len(list)-1:
    print(list[K])
else:
    K = K - len(list) + 1
    print(replist[( K % len(replist) ) -1])

