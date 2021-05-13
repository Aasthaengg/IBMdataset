# input
N = int(input())
D, X = map(int, input().split())
A = [int(input()) for n in range(N)]

# check
for a in A:
    X += len(list(range(1, D + 1, a)))

print(X)
