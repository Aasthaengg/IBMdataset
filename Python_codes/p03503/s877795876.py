n = int(input())
opened = [int('0b' + input().replace(' ', ''), 2) for i in range(n)]
prise = [list(map(int, input().split())) for i in range(n)]

ans = -float('INF')
for i in range(1,int('10000000000', 2)):
    cnt = [0 for i in range(n)]
    for j in range(10):
        if 1<<j & i == 0:
            continue
        for k in range(n):
            if 1<<j & opened[k]:
                cnt[k] += 1
    tmp = sum([prise[k][cnt[k]] for k in range(n)])
    if tmp > ans:
        # print(bin(i), tmp, [prise[k][cnt[k]] for k in range(n)], cnt)
        ans = tmp
print(ans)
# print(bin(2^10-1))
# [print(bin(i)) for i in opened]
