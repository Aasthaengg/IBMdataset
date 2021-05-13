N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

A = []
C = []
for a, b in AB:
  A.append(a)
  C.append(a + b)
#print("C:", C)

C.sort()
C = C[::-1]

print(sum(A) - sum(C[1::2]))