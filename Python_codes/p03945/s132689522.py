S = input()
now = 1
cnt = 0
for s in S:
    if s != now:
        now = s
        cnt += 1
print(cnt -1)