from itertools import accumulate
N, M, K = map(int,input().split())
A_list = [0] + list(map(int,input().split()))
B_list = [0] + list(map(int,input().split()))
A_sums_list = list(accumulate(A_list))
B_sums_list = list(accumulate(B_list))
ans = 0
for i, A_sums in enumerate(A_sums_list):
    B_min = -1
    B_max = M + 1
    while B_max - B_min > 1:
        B_index = int((B_max + B_min) * 0.5)
        if A_sums + B_sums_list[B_index] <= K:
            B_min = B_index
        else:
            B_max = B_index
    B_index = int((B_max + B_min) * 0.5)
    if i + B_index > ans and A_sums + B_sums_list[B_index] <= K:
        ans = i + B_index
print(ans)