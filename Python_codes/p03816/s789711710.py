N = int(input())
A = list(map(int, input().split()))
q = len(set(A))
if q % 2 == 0:
    print(q - 1)
else:
    print(q)
