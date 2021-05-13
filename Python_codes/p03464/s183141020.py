import math
K = int(input())
A = [int(i) for i in input().split()][::-1]

if A[0] != 2:
    print(-1)
    exit()

ans_low = 2
ans_high = 3

for i in range(1, K):
    next_ans_high = ((ans_high//A[i])+1)*A[i]-1
    next_ans_low = math.ceil(ans_low/A[i])*A[i]

    if (next_ans_high // A[i])*A[i] > ans_high or next_ans_low > next_ans_high:
        print(-1)
        exit()

    ans_high = next_ans_high
    ans_low = next_ans_low

    # print(A[i], ans_low, ans_high)

print(ans_low, ans_high)
