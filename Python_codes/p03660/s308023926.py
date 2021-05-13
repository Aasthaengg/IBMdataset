from collections import deque

N = int(input())

dic = {}

for i in range(N-1):

    a,b = map(int,input().split())
    a -= 1
    b -= 1

    if a not in dic:
        dic[a] = []
    if b not in dic:
        dic[b] = []

    dic[a].append(b)
    dic[b].append(a)

alis = [""] * N
alis[0] = 0

Q = deque([])
Q.append(0)

while len(Q) > 0:

    now = Q.pop()

    if now not in dic:
        continue

    for b in dic[now]:

        if alis[b] == "":
            alis[b] = alis[now] + 1

            Q.append(b)

blis = [""] * N
blis[N-1] = 0

Q = deque([])
Q.append(N-1)

while len(Q) > 0:

    now = Q.pop()

    if now not in dic:
        continue

    for b in dic[now]:

        if blis[b] == "":
            blis[b] = blis[now] + 1

            Q.append(b)

F = 0
S = 0

for i in range(N):
    if alis[i] <= blis[i]:
        F += 1
    else:
        S += 1

if F <= S:
    print ("Snuke")
else:
    print ("Fennec")

