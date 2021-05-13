n,q = map(int,input().split())

queue = []

for _ in range(n):
    name, time = input().split()
    time = int(time)
    queue.append([name,time])

time = 0
ans = []

while queue:
    tmp = queue.pop(0)
    if tmp[1] > q:
        tmp[1] -= q
        time += q
        queue.append(tmp)
    else:
        time += tmp[1]
        ans.append((tmp[0],time))

for x in ans:
    print(x[0], x[1])
