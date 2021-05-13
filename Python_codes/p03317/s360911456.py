N,K = map(int,input().split())

a = list(map(int,input().split()))

cnt = 1

ans = K

while ans < N:
    cnt += 1
    ans += K-1

print(cnt)