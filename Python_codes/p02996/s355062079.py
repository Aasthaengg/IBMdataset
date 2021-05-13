N = int(input())

C = []
for _ in range(N):
    a, b = map(int, input().split())
    C.append((a, b))
C = list(sorted(C, key=lambda x: x[1]))

t = 0
for a, b in C:
    if t + a > b:
        print("No")
        break
    t += a
else:
    print("Yes")
