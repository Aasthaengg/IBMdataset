def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0 for _ in range(N)]
    ans = [] 
    for i in range(N, 0, -1):
        cnt = 0
        mul = 2
        while i*mul-1 < N:
            cnt += B[i*mul-1]
            mul += 1
        if A[i-1] == cnt%2:
            B[i-1] = 0
        else:
            B[i-1] = 1
            ans.append(i)
    print(len(ans))
    if len(ans) != 0:
        print(*ans)

    

if '__main__' == __name__:
    resolve()
