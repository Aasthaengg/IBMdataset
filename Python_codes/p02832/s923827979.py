N = int(input())
lis = list(map(int, input().split()))
cnt = 0

if 1 not in lis:
    cnt = -1
else:
    for idx, val in enumerate(lis):
        if val != idx+1-cnt:
            cnt += 1

print(cnt)