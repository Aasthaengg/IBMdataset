N = int(input())
A = [""] * N
B = [0] * N
for i in range(N):
    s, t = input().split()
    A[i] = s
    B[i] = int(t)
X = input()
c = 0
for i in range(N):
    c += B[i]
    if A[i] == X:
        print(sum(B) - c)
        exit()
