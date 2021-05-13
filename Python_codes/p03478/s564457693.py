N, A, B = map(int, input().split())

ans_list = []
for i in range(N + 1):
    n = i
    local_sum = 0
    for j in reversed(range(len(str(i)))):
        local_sum += n // (10 ** j)
        n -= n // (10 ** j) * (10 ** j)
    if A <= local_sum and local_sum <= B:
        ans_list.append(i)
print(sum(ans_list))