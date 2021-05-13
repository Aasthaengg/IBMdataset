import sys
n, q = map(int, input().split())
queue = [[label, int(num)] for label, num in map(lambda line: line.strip().split(), sys.stdin.readlines())] 
i = 0
time = 0
while len(queue) > 0:
    i = i % len(queue)
    time += q
    queue[i][1] -= q
    if queue[i][1] <= 0:
        time += queue[i][1]
        print("{} {}".format(queue[i][0], time))
        queue.pop(i)
        i -= 1
    i += 1
