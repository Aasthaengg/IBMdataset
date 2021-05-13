n = int(input())
count = 0
for i in range(n+1):
    hoge = i
    cnt = 0
    while hoge > 0:
        hoge //= 10
        cnt += 1
    if cnt % 2 != 0:
        count += 1
print(count)