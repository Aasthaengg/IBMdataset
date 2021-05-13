n = int(input())
A = [0]
for _ in range(n):
    A.append(int(input()))

seen = set()
up = 1
cnt = 0
while up != 2:
    if up in seen:
        cnt = -1
        break
    seen.add(up)
    up = A[up]
    cnt += 1

print(cnt)
