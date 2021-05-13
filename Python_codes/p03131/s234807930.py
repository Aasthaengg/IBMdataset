def f():
    K, A, B = map(int, input().split())

    if A+1 >= B:
        print(K+1)
        return

    if K <= A:
        print(K+1)
        return

    res = A

    K -= A-1
    if K % 2 == 1:
        res += 1
        K -= 1

    res += (K//2) * (B-A)
    
    print(res)
    return

f()