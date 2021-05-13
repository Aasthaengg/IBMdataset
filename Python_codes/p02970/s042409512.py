n, d = list(map(int, input().split()))
cnt = 0
while n>0:
    n -= 2*d + 1
    cnt += 1
print(cnt)