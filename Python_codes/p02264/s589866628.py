from queue import deque

def main():
    n, q = tuple(map(int, input().split(' ')))

    task_q = deque()
    for idx in range(n):
        l = input().split(' ')
        task_q.append((l[0], int(l[1])))

    tot_time = 0
    while len(task_q) != 0:

        task = task_q.popleft()
        if task[1] > q:
            task_q.append((task[0], task[1] - q))
            tot_time += q

        else:
            tot_time += task[1]
            print(task[0], tot_time)


main()
