def solv():
    n = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    ans = 0

    for i in range(n):
        x = A[i] + A[i+1]
        ans += min(x,B[i])
        A[i+1] = min(A[i+1],max(x-B[i],0))
    return print(ans)

solv()
