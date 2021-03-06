import bisect

N = int(input())
A = [int(input()) for _ in range(N)]
sort_A = sorted(A)
max_val = max(A)
second_val = sort_A[bisect.bisect_right(sort_A, max_val) - 2]

for i in range(N):
    if A[i] == max_val:
        print(second_val)
    else:
        print(max_val)