import math
N, H = map(int, input().split())
A = 0
B = []
ans = 0
for _ in range(N):
    a, b = map(int, input().split())
    A = max(A, a)
    B.append(b)
B.sort(reverse=True)
for i in range(N):
    if B[i] < A:
        break
    if H <= 0:
        print(ans)
        exit()
    H -= B[i]
    ans += 1
if H % A == 0:
    ans += H // A
    print(ans)
else:
    ans += math.ceil(H / A)
    print(ans)