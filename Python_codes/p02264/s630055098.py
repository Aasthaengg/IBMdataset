import sys
n, q = map(int, sys.stdin.readline().split())
processes = []
for i in range(n):
    name, time =sys.stdin.readline().split()
    processes += [[name, int(time)]]

progress = 0

while len(processes):
    new_processes = []
    for target in processes:
        if target[1] > q:
            target[1] -= q
            progress += q
            new_processes += [target]
        else:
            progress += target[1]
            print(target[0], progress)
    processes = new_processes