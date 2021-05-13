K, A, B = map(int, input().split())
if A + 1 >= B or K < A + 1: result = K + 1
else:
    K -= A-1
    result = A + K//2 * (B - A)
    if K%2 == 1: result += 1
print(result)