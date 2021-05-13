N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

cnt = 0
for a, b in zip(A[::-1], B[::-1]):
    v = (a + cnt) % b
    # print(f'{v=}')
    if v == 0:
        continue
    cnt += b - v
print(cnt)
