def selection_sort(A):
    steps = 0
    N = len(A)
    for i in range(0, N):
        minj = i
        for j in range(i, N):
            if A[minj][0] > A[j][0]:
                minj = j
        if i != minj:
            steps += 1
        A[minj], A[i] = A[i], A[minj]

    # [print(A[idx], end=' ') if idx != len(A) - 1 else print(A[idx]) for idx in range(len(A))]
    # print(steps)
    return A


def bubbleSort(A):
    steps = 0
    flag = 1
    completed_idx = 0
    while flag:
        flag = 0
        for i in range(len(A) - 1, completed_idx, -1):
            if A[i - 1][0] > A[i][0]:
                A[i - 1], A[i] = A[i], A[i - 1]
                steps += 1
                flag = 1
        completed_idx += 1

    # for e in A[:-1]:
    #     print(e, end=' ')
    # print(A[-1])
    # print(steps)
    return A

d = dict()
N = int(input())
A = [(int(elem[1:]), elem[0]) for elem in input().split()]

for elem in A:
    if elem[0] not in d:
        d[elem[0]] = elem[1]
    else:
        d[elem[0]] += elem[1]

is_stable = True
A_bubble = bubbleSort(A[:])
st = A_bubble[0][1]
cur_val = A_bubble[1][0]
prev_val = A_bubble[0][0]
for e in A_bubble[1:]:
    cur_val = e[0]
    if cur_val != prev_val:
        if st != d[prev_val]:
            is_stable = False
            break
        st = ''
    st += e[1]
    prev_val = cur_val
[print(A_bubble[idx][1] + str(A_bubble[idx][0]), end=' ') if idx != len(A_bubble) - 1 else print(A_bubble[idx][1] + str(A_bubble[idx][0])) for idx in range(len(A_bubble))]
print('Stable' if is_stable else 'Not stable')

is_stable = True
A_slt = selection_sort(A[:])
st = A_slt[0][1]
cur_val = A_slt[1][0]
prev_val = A_slt[0][0]
for e in A_slt[1:]:
    cur_val = e[0]
    if cur_val != prev_val:
        if st != d[prev_val]:
            is_stable = False
            break
        st = ''
    st += e[1]
    prev_val = cur_val

[print(A_slt[idx][1] + str(A_slt[idx][0]), end=' ') if idx != len(A_slt) - 1 else print(A_slt[idx][1] + str(A_slt[idx][0])) for idx in range(len(A_slt))]
print('Stable' if is_stable else 'Not stable')
#
# 5
# H4 C9 S4 D2 C3
