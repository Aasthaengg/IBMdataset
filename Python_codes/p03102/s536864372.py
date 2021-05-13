N, M, C = map(int, input().split())
B_list = list(map(int, input().split()))
A_lists = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for A_list in A_lists:
    tmp = [a * b for a, b in zip(A_list, B_list)]
    tmp = sum(tmp) + C
    if tmp > 0:
        cnt += 1
print(cnt)