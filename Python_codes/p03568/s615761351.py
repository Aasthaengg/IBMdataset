n = int(input())
lis =list(map(int, input().split()))

cnt = 1

for i in lis:
    if i % 2 == 0:
        cnt *= 2

print(3**n - cnt)