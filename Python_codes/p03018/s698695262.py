s = input()

s = s.replace("BC", "D")

ans = 0
a_cnt = 0
for e in s:
    if e == "A":
        a_cnt += 1

    elif e == "D":
        ans += a_cnt

    else:
        a_cnt = 0

print(ans)
