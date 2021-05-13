from collections import deque, namedtuple

Process = namedtuple('Process', 'name, time')

def main():
    n, q = map(int, input().split())
    dq = deque()
    for _ in range(n):
        name, time = input().split()
        dq.append(Process(name, int(time)))
    cur_time = 0
    while len(dq) > 0:
        x = dq.popleft()
        if x.time > q:
            dq.append(Process(x.name, x.time-q))
            cur_time += q
        else:
            cur_time += x.time
            print(x.name, cur_time)


if __name__ == '__main__':
    main()
