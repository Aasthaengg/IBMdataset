N = int(input())
A = list(map(int, input().split()))

def f():
    for i in range(1, N):
        if A[i-1] < A[i]:
            state = 0
            break
        if A[i-1] > A[i]:
            state = 1
            break
    else:
        print(1)
        return

    cnt = 1

    for i in range(1, N):
        if A[i-1] < A[i]:
            if state == 1:
                state = 2
                cnt += 1
            else:
                state = 0

        if A[i-1] > A[i]:
            if state == 0:
                state = 2
                cnt += 1
            else:
                state = 1
    
    print(cnt)

f()