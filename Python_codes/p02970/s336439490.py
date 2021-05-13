n,d  = list(map(int,input().split()))

ans = 0
cnt = 0
while ans < n:
    ans += d*2+1
    cnt += 1

print(cnt)