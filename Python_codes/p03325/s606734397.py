N = int(input())
A = [int(a) for a in input().split()]

num_f2 = [0] * N
for i in range(N):
    a = A[i]
    while True:
        if a % 2 == 0:
            num_f2[i] += 1
            a //= 2
        else:
            break

print(sum(num_f2))