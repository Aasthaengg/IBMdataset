import sys
N,M = map(int,input().split())
students = [None] * N
checkpoints = [None] * M
for student in range(0,N):
    students[student] = list(map(int,input().split()))
for checkpoint in range(0,M):
    checkpoints[checkpoint] = list(map(int,input().split()))

if N < 0 or N > 50 or M < 0 or M > 50:
    sys.exit()
for student in students:
    if student[0] < -100000000 or student[1] > 100000000:
        sys.exit()
for checkpoint in checkpoints:
    if checkpoint[0] < -100000000 or checkpoint[1] > 100000000:
        sys.exit()

distance = [40000000000000000] * N
result = [0] * N
count = 0
for student in students:
    checkpoint_count = 0
    for checkpoint in checkpoints:
        tmp_distance = int(abs(student[0] - checkpoint[0]) + abs(student[1] - checkpoint[1]))
        if int(distance[count]) > int(tmp_distance):
            distance[count] = tmp_distance
            result[count] = checkpoint_count + 1
        checkpoint_count += 1
    count += 1

for I in result:
    print(I)