N = int(input())
A = tuple(map(int, input().split(' ')))
B = tuple(map(int, input().split(' ')))
C = tuple(map(int, input().split(' ')))

s = sum(B)
s += sum([C[a1 - 1] for a1, a2 in zip(A, A[1:]) if a2 - a1 == 1])

print(s)
