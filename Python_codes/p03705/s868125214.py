N, A, B = map(int, input().split())

if B < A:
    print(0)
    exit()

if N == 1 and B != A:
    print(0)
    exit()

print((B-A)*(N-2)+1)    