N, H, W = map(int, input().split())
cnt = 0
for _ in range(N):
    A, B = map(int, input().split())
    cnt += H <= A and W <= B
print(cnt)