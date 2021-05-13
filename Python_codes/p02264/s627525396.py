def parse(l):
    name, time = l.split()
    return (name, int(time))


n, q = map(int, input().split())
queue = list(parse(input()) for _ in range(n))
time = 0

while queue:
    (name, remain_time) = queue.pop(0)
    if remain_time > q:
        time += q
        queue.append((name, remain_time - q))
    else:
        time += remain_time
        print(name, time)