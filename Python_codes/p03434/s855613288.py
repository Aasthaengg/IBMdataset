N = int(input())
a = list(map(int, input().split()))
a_sorted = sorted(a, reverse = True)

A, B = 0, 0

for i in range(N):
    if i % 2 == 0:
        A += a_sorted[i]
    else:
        B += a_sorted[i]

print(A-B)