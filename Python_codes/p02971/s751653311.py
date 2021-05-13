N = int(input())
A = [int(input()) for j in range(N)]

B = sorted(A)
a = B[-1]
b = B[-2]
c = A.index(a)
for j in range(N):
    if j == c:
        print(b)
        continue
    print(a)