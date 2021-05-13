n = int(input())
A = list(map(int, input().split()))

B1 = [(-1)**i for i in range(n)]
B2 = [(-1)**(i+1) for i in range(n)]

def func(A, B):
    cum = 0
    res = 0
    for i in range(n):
        cum += A[i]
        if B[i] > 0 and cum <= 0:
            res += 1-cum
            cum = 1
        elif B[i] < 0 and cum >= 0:
            res += cum+1
            cum = -1
    return res
     
print(min(func(A, B1), func(A, B2)))
