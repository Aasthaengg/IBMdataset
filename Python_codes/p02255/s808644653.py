n = input()
A = [int(i) for i in input().split(' ')]

def trace(A):
    for index, v in enumerate(A):
        print(v, end='')
        if index != len(A) - 1:
            print(' ', end='')
    print()

trace(A)
# algorithm
# for i in range(1, len(A)):
#     v = A[i]
#     j = i - 1
#     while j >= 0 and A[j] > v:
#         A[j+1] = A[j]
#         j -= 1
#     A[j+1] = v
#     trace(A)

for index, value in enumerate(A):
    if index == 0:
        continue

    prev_idx = index - 1
    while prev_idx >= 0 and A[prev_idx] > value:
        A[prev_idx + 1] = A[prev_idx]
        prev_idx -= 1
    A[prev_idx + 1] = value
    trace(A)