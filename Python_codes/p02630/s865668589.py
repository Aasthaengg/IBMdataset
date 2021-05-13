n = int(input())
A = [0] * (10**5+1)

B = list(map(int, input().split()))

for i in B:
    A[i] += 1

m = int(input())

sum_a = sum(B)

for _ in range(m):
    a, b = map(int, input().split())
    sum_a = sum_a + (b - a) * A[a]
    A[b] += A[a]
    A[a] = 0
    print(sum_a)