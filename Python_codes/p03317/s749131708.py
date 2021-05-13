N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = 1
length = K
while True:
    if length >= N:
        print(cnt)
        break
    length += K-1 
    cnt += 1