S = list(map(str, input().split()))
A = list(map(int, input().split()))
U = input()

ind = S.index(U)

A[ind] -= 1

print(" ".join(list(map(str, A))))
