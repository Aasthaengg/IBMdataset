st = list(map(lambda x: x=='B',input()))[::-1]

ans = 0

count = 0

for i, v in enumerate(st):
    if v:
        ans += i - count
        count += 1

print(ans)