N = int(input())
H = [[0]*N for _ in range(100)]
for j, h in enumerate(map(int, input().split())):
    for i in range(h):
        H[i][j] = 1
cnt = 0
for i in range(100):
    a0 = 0
    for a in H[i]:
        if a != a0 and a0==0:
            cnt += 1
        a0 = a
print(cnt)