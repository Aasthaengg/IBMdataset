A,B = map(int,input().split())

ans = 1
cnt = 0
while True:
    cnt += 1
    if ans >= B:
        break
    ans += A-1

print(cnt-1)