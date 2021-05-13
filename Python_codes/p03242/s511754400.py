n = str(input())

ans = 0
if n[0] == "1":
    ans += 900
else:
    ans += 100

if n[1] == "1":
    ans += 90
else:
    ans += 10

if n[2] == "1":
    ans += 9
else:
    ans += 1

print(ans)