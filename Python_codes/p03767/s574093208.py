N = int(input())

A = list(map(int, input().split()))

A_sorted = sorted(A, reverse = True)

strength = 0

for i in range(N):
    strength += A_sorted[2*i+1]

print(strength)