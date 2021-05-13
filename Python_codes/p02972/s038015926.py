import numpy as np

N = int(input())
A = np.array(list(map(int, input().split())))
ans_list = np.zeros(N).astype(int)
N_2 = N // 2
ans = 0
for i in range(N):
    tmp = N - i - 1
    # print(tmp)
    if i < N_2:
        ans_list[tmp] = A[tmp]
        if A[tmp] == 1:
            ans += 1
    else:
        add = (np.sum(ans_list[tmp::(tmp + 1)]) + A[tmp]) % 2
        ans_list[tmp] = add
        if add == 1:
            ans += 1

print(ans)
for i in range(N):
    if ans_list[i] == 1:
        if i == N - 1:
            print(i + 1, end="")
        else:
            print(i + 1, end=" ")
