N = int(input())

A = [1]
for _ in range(N):
    A.append(int(input()))

used = set()

i = 0
ans = 0
while True:
    a = A[i]

    if a == 2:
        print(ans)
        break

    if a in used:
        print(-1)
        break

    used.add(i)
    i = a
    ans += 1
