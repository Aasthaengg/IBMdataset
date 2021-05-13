n = int(input())
a = [int(i) for i in input().split()]

cnt = 0
for i in a:
    while i % 2 == 0:
        cnt += 1
        i /= 2
print(cnt)