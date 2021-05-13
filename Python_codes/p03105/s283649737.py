a, b, c = map(int, input().split())
cnt = 0
while cnt < c and a <= b:
    b -= a
    cnt += 1
print(cnt)