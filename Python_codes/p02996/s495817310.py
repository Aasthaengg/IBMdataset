N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
AB.sort(key=lambda x: x[1])
A, B = [list(i) for i in zip(*AB)]
t = 0
bl = True
for i in range(N):
    t += A[i]
    if t > B[i]:
        bl = False

print('Yes' if bl else 'No')