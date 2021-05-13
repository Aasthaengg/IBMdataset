A, B, K = list(map(int, input().split()))
flag = 0
def f(a, b):
    return a // 2, b + a //2
flag = 0
for i in range(K):
    if flag == 0:
        A, B = f(A, B)
        flag = 1
    else:
        B, A = f(B, A)
        flag = 0
print(A, B)
