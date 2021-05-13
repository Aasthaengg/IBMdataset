n, x = map(int, input().split())
data = [0] + list(map(int, input().split()))
count = 0
tmp = 0
for d in data:
    tmp += d
    if tmp <= x:
        count += 1
    # print(tmp)

print(count)