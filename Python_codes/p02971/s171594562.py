N = int(input())
A = [int(input()) for _ in range(N)]
A_cpy = A[:]
A_cpy.sort()
max_ = A_cpy[-1]

for a in A:
    if a == max_:
        print(A_cpy[-2])
    else:
        print(max_)