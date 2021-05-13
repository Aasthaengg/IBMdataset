a = input()
N = int(a)
A = [int(input()) for i in range(N)]
ind = A.index(max(A))
max = max(A)

for i in range(N):
    if i == ind:
        B = sorted(A)
        print(B[N-2])
    else:
        print(max)