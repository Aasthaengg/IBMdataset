N, H, W = [int(_) for _ in input().split()]

cnt = 0
for _ in range(N):
    A, B = [int(_) for _ in input().split()]
    if H <= A and W <= B:
        cnt += 1
print(cnt)
