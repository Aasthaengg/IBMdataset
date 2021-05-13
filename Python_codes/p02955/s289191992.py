import math
N, K = map(int, input().split())

A_array = list(map(int, input().split()))

# print(A_array)

A_sum = sum(A_array)

candidate_array = []

for i in range(1, int(math.sqrt(A_sum))+1):
    if A_sum % i == 0:
        candidate_array.append(i)
        if A_sum // i != i:
            candidate_array.append(A_sum//i)

candidate_array.sort()

ans = 0

for check_num in candidate_array:
    q_array = [a % check_num for a in A_array]
    q_array.sort()
    # print(q_array)
    start = 0
    rest = N * check_num - sum(q_array)
    for q in q_array:
        start += q
        rest -= (check_num-q)
        # print(start,rest)
        if start == rest:
            break
    if start <= K:
        ans = max(ans, check_num)

print(ans)
