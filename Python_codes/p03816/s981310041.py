

N = int(input())
A = list(map(int, input().split()))
setA = set(A)
if len(setA) % 2 != 0:
    print(len(setA))
else:
    print(len(setA) - 1)