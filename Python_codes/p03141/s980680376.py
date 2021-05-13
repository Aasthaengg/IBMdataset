N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

A = [a for a, b in AB]
C = [a + b for a, b in AB]
C.sort()
C = C[::-1]
print(sum(A) - sum(C[1::2]))