x = input()
cnt = 0
ans = len(x)
for s in x:
    if s == "S":
        cnt += 1
    else:
        if 0 < cnt:
            cnt -= 1
            ans -= 2
print(ans)