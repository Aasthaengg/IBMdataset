S = input().split(" ")
N = int(S[0])
M = int(S[1])

def calculate(n,m):

    if n == 1 and m == 1:
        return 1

    if n == 1:
        return m - 2

    if m == 1:
        return n - 2

    return (n - 2) * (m - 2)
result = calculate(N,M)
print(result)