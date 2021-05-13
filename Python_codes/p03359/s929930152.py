month, day = map(int, input().split())

if (day >= month):
    cnt = month
else:
    cnt = month - 1


print(cnt)