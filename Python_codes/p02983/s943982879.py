l, r = map(int, input().split())
ll = l % 2019
rr = r % 2019
minn = 2019
if r - l > 2019:
    rr += 2019
for i in range(ll, rr):
    for j in range(ll + i - ll + 1, rr + 1):
        if minn > i * j % 2019:
            minn = i * j % 2019
print(minn)
