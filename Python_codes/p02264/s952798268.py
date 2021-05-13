# Aizu Problem ALDS_1_3_B: Queue
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")


N, quantum = [int(_) for _ in input().split()]
queue = []
for _ in range(N):
    name, length = input().split()
    queue.append([name, int(length)])

time = 0
while len(queue) > 0:
    name, length = queue.pop(0)
    if length > quantum:
        time += quantum
        queue.append([name, length - quantum])
    else:
        time += length
        print(name, time)