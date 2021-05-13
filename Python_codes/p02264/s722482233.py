#coding:utf-8
#1_3_B
n, q = map(int, input().split())
total_time = 0
queue = [input().split() for i in range(n)]

while queue:
    ps = queue.pop(0)
    time = int(ps[1])

    if time <= q:
        total_time += time
        print(ps[0], total_time)
    else:
        total_time += q
        time -= q
        ps[1] = time
        queue.append(ps)