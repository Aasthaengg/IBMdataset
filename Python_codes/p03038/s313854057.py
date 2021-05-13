def check():
    N, M = map(int, input().split())
    A = sorted([int(i) for i in input().split()])
    sousa = sorted([[int(i) for i in input().split()] for i in range(M)],
                   reverse=True, key=lambda x:x[1])
    index = 0
    for cnt, value in sousa:
        for i in range(cnt):
            if index == N:
                break
            if A[index] < value:
                A[index] = value
            else:
                return(sum(A))
            index += 1
    return(sum(A))
print(check())