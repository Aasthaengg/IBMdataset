def insertion_sort(A, N, gap):
    cnt = 0
    for i in range(gap, N):
        tmp = A[i]
        j = i - gap
        while j>=0 and A[j] > tmp:
            A[j+gap] = A[j]
            j = j - gap
            cnt = cnt + 1
        A[j+gap] = tmp
    return cnt

def shell_sort(A, N):
    cnt = 0
    gaps = [int((3**item-1)/2) for item in range(1, 100) if int((3**item-1)/2) <= N][::-1]
    m = len(gaps)
    for gap in gaps:
        cnt = cnt + insertion_sort(A, N, gap)
    print(m)
    print(' '.join([str(gap) for gap in gaps]))
    print(cnt)
    for i in range(0, N):
        print(A[i])


N = int(input())
A = [int(input()) for i in range(N)]

shell_sort(A, N)