n = int(input())
string = input()
ans = 0
now = 0
for s in string:
    if s == "I":
        now += 1
        ans = max(ans, now)
    else:
        now -= 1
print(ans)
