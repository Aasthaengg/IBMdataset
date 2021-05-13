n,q = map(int, input().split())
que = []
t = 0
for i in range(n):
    que.append(input().split())

while len(que) != 0:
    proc =  que.pop(0)
    if int(proc[1]) <= q:
        t += int(proc[1])
        print(proc[0],t)
    else:
        t += q
        proc[1] = int(proc[1]) - q
        que.append(proc)