A, B, K = map(int,input().split())

def calc(a, b):
    if a %  2 != 0:
        a -= 1
    a //= 2
    b += a
    return a, b


for i in range(K):
    if i % 2 == 0:
        A, B = calc(A, B)
    else:
        B, A = calc(B, A)

print(A, B)


