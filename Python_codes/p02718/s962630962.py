def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    sum = 0
    for i in range(N):
        sum += A[i]

    cnt = 0
    tmp = sum/(4*M)
    for i in range(N):
        if A[i] >= tmp:
            cnt += 1

    if cnt >= M:
        print('Yes')
    else:
        print('No')

main()
