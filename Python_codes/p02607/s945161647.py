n = int(input())
a = list(map(int, input().split()))
aa = a[::2]

cnt = 0
for i in aa:
    if i % 2 == 1:
        cnt += 1

print(cnt)
