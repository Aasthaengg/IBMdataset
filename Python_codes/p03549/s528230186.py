N, M = map(int, input().split())
 
x = (100 * (N - M) + 1900 * M)
e = x * (2 ** M)
print(e)