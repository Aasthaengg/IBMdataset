X = int(input())
n = 100
cnt = 0
while n < X:
    n = n * 101 // 100
    cnt += 1
print(cnt)