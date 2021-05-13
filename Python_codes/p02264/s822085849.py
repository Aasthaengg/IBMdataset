#!/usr/bin/env python3

import sys


def main():
    lines = sys.stdin.readlines()
    (_, quantum) = lines[0].split(' ')
    quantum = int(quantum)

    processes = []
    for line in lines[1:]:
        if line.strip() == '':
            break

        (k, v) = line.strip().split(' ')
        processes.append((k, int(v)))

    time = 0
    result = []
    while True:
        (process, process_time) = processes.pop(0)  # Dequeue

        if process_time <= quantum:
            time += process_time
            result.append((process, time))
        else:
            time += quantum
            processes.append((process, process_time - quantum))

        if len(processes) == 0:
            break

    for item in result:
        print("%s %s" % (item[0], item[1]))

if __name__ == "__main__":
    main()