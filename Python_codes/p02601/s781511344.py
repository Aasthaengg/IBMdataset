A, B, C = [int(_) for _ in input().split()]
K = int(input())

k = 0
while A >= B:
    B *= 2
    k += 1
while B >= C:
    C *= 2
    k += 1

if k <= K:
    print("Yes")
else:
    print("No")
