s = input()
t = "BDEFHIJKLMNOPQRSUVWXYZ"
res = ""
for x in s:
    if x in t:
        res += "0"
    else:
        res += x
ans = 0
for a in res.split("0"):
    ans = max(ans, len(a))
print(ans)
