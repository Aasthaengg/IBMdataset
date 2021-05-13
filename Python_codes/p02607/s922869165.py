N = int(input())
vals = list(map(int, input().split()))
cnt = 0

for ad, val in enumerate(vals, 1):
    if ad % 2 == 1 and val % 2 == 1:
        cnt += 1
print(cnt) 