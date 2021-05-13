K = int(input())

seen = set()
extra = 7 % K
cnt = 1
seen.add(extra)
while extra != 0:
    extra = (extra * 10 + 7) % K
    if extra in seen:
        print(-1)
        exit()
    seen.add(extra)
    cnt += 1

print(cnt)