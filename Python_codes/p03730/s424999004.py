A, B, C = map(int, input().split())
N = A % B
M, i = 0, 2
while M != N:
    M = i * N % B
    if M == C:
        print("YES")
        break
    i += 1
else:
    print("NO")