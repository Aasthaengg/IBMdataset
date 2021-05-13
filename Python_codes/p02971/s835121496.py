N = int(input())
A = [int(input()) for _ in range(N)]
A_s = sorted(A, reverse = True)


A_max = A_s[0]
A_max2 = A_s[1]

for i in A:
    if i == A_max:
        print(A_max2)
    else:
        print(A_max)
