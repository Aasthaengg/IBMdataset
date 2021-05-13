n, q = map(int, input().split())

processes = []

for i in range(int(n)):
    process_name, process_time = input().split()
    processes.append([process_name, int(process_time)])

elapsed_time = 0
while len(processes):
    process = processes.pop(0)
    if process[1] > q:
        process[1] -= q
        processes.append(process)
        elapsed_time += q
    else:
        elapsed_time += process[1]
        print(process[0], elapsed_time)