A, B, N = map(int, input().split())
def calc(x):
    return int(A*x/B) - A*int(x/B)

if N < B:
    print(calc(N))
else:
    print(calc(B-1))