n,d = map(int,input().split())
r = d * 2 + 1
cnt = 0

while n > 0:
    n = n - r
    cnt += 1

print(cnt)