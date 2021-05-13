a,b = map(int,input().split())
m = 1
cnt = 0
while m < b:
    m -= 1
    m += a
    cnt += 1
print(cnt)
