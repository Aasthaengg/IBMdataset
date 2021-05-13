N,K = map(int,input().split())
A = list(map(int,input().split()))

def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a%b)

if K > max(A):
    print("IMPOSSIBLE")
else:
    now = A[0]
    for i in range(1,N):
        now = euclid(now,A[i])

    if now == 1:
        print("POSSIBLE")
    elif K % now == 0:
        print("POSSIBLE")
    elif K in A:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")