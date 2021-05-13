N = int(input())
A = sorted(list(map(int, input().split())),reverse=True)

Alice = sum(A[0::2])
Bob = sum(A) -Alice
print(Alice-Bob)