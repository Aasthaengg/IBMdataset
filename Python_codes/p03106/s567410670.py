def resolve():
    A, B, K = list(map(int, input().split()))
    cnt = 0
    i = max(A, B)
    while True:
        if A%i==0 and B%i==0:
            cnt += 1
            if cnt == K:
                break
        i -= 1
    print(i)

if '__main__' == __name__:
    resolve()