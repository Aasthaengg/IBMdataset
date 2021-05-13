N = int(input())
A, B = [], []
for _ in range(N):
    a, b = map(int, input().split(" "))
    A.append(a)
    B.append(b)

ans = 0
added = 0
for a, b in zip(A[::-1], B[::-1]):
    if (a + added) % b != 0:
        ans += b - (a + added) % b
        added += b - (a + added) % b
print(ans)