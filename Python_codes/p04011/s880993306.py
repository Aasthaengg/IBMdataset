N = int(input())
K = int(input())
X = int(input())
Y = int(input())
k = 1 
result = 0
if K < N:
    while k <= K:

        result += X
        k += 1
    while k <= N:

        result += Y
        k += 1
if K >= N:
    while k <= N:
        result += X
        k += 1
print(result)
