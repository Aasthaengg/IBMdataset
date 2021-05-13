def fib(n):
    if n <= 1:
        return n
    result = [1, 0, 0, 1]
    matrix = [1, 1, 1, 0]
    while n > 0:
        if n % 2:
            result = mul(matrix, result)
        matrix = mul(matrix, matrix)
        n //= 2
    return result[2]

def mul(a, b):
    return [a[0]*b[0] + a[1]*b[2],
            a[0]*b[1] + a[1]*b[3],
            a[2]*b[0] + a[3]*b[2],
            a[2]*b[1] + a[3]*b[3]]
    
N, M = map(int, input().split())
if N == 1:
    print(1)
    quit()
S = [-1]
for i in range(M):
    S.append(int(input()))
S.append(N + 1)
S = [S[i + 1] - S[i] for i in range(M + 1)]
if any([x == 1 for x in S]):
    print(0)
    exit()
num = 1
for x in S:
    num *=  fib(x - 1)
    num = num % 1000000007
print(num)