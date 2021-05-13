from collections import defaultdict
H, W, N = map(int, input().split())
A = defaultdict(int)

for i in range(N):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    for j in range(-1, 2):
        for k in range(-1, 2):
            if 1 <= a + j < H - 1 and 1 <= b + k < W - 1:
                A[(a + j, b + k)] += 1
                
print((H - 2) * (W - 2) - len(A))
                
for i in range(1, 10):
    cnt = 0
    for v in A.values():
        if v == i:
            cnt += 1
    print(cnt)