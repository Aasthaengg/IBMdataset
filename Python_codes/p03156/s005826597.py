N = int(input())
A, B = map(int, input().split())
P = list(map(int, input().split()))

first_cnt = 0
second_cnt = 0
third_cnt = 0

for i in range(N):
    if P[i] <= A:
        first_cnt += 1
    elif P[i] <= B:
        second_cnt += 1
    else:
        third_cnt += 1

print(min(first_cnt, second_cnt, third_cnt))