n = int(input())
s = input()
cnt = s.count(".")
ans = cnt

for c in s:
    if c == "#":
        cnt += 1
    else:
        cnt -= 1
    ans = min(ans, cnt)

print(ans)