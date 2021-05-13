# author:  Taichicchi
# created: 17.09.2020 23:46:19


N = int(input())

S = input()

cnt = 0

for i in map(lambda x: str(x).zfill(3), range(1000)):
    f = 0
    for s in S:
        if s == i[f]:
            f += 1
        if f == 3:
            break
    if f == 3:
        cnt += 1

print(cnt)
