import sys
n = int(input())
input_line = [[int(i) for i in str.split()] for str in sys.stdin.read().splitlines()]
for i in range(n):
    input_line[i] = [] if len(input_line[i]) == 2 else input_line[i][2:]
detect_time = [0] * n
finish_time = [0] * n
is_visit = [False] * n
stack = []
time = 0

while(time < n*2):
    time += 1
    id = is_visit.index(False) + 1
    stack.append(id)
    is_visit[id-1] = True
    detect_time[id-1] = time
    while(len(stack) != 0):
        id = stack[-1]
        if len(input_line[id-1]) == 0:
            time += 1
            finish_time[stack.pop()-1] = time
        else:
            detect_id = input_line[id-1].pop(0)
            if is_visit[detect_id-1]:
                continue
            stack.append(detect_id)
            time += 1
            detect_time[detect_id-1] = time
            is_visit[detect_id-1] = True


for id in range(n):
    print('{0} {1} {2}'.format(id+1, detect_time[id], finish_time[id]))
