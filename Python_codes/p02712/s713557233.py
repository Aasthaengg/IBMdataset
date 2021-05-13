result = 0
N = int(input())
for N in list(range(1, N+1)):
    if int(N % 3 != 0) and int(N % 5 != 0):
        result = result + N
print(result)
