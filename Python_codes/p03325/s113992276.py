n = int(input())
lis = list(map(int, input().split()))

cnt = 0
nlis = []

for i in lis:
    if i % 2 == 0:
        nlis.append(i)

if nlis == []:
    print(0)
    exit()
else:
    for m in nlis:
        while m > 1:
            m //= 2
            cnt += 1
            if m % 2 == 1:
                break

print(cnt)