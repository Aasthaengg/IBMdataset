N = int(input())
A = list(map(int, input().split()))
kinds = set(A)

dif = N - len(kinds)
if dif % 2 == 0:
    print(len(kinds))
else:
    print(len(kinds) - 1)
