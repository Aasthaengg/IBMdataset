def main():
    process, quantum = input().split()
    process = int(process)
    quantum = int(quantum)
    processes = []
    for i in range(process):
        t, u = input().split()
        processes.append((t, int(u)))
    ptime = 0
    while len(processes) > 0:
        t = processes.pop(0)
        if t[1] > quantum:
            processes.append((t[0], t[1]-quantum))
            ptime += quantum
        else:
            ptime += t[1]
            print(t[0] + " " + str(ptime))




if __name__ == "__main__":
    import os
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == "-d":
            fd = os.open("input.txt", os.O_RDONLY)
            os.dup2(fd, sys.stdin.fileno())
            main()
    else:
        main()