s = input()
q = int(input())
rev = False
bef = ""
aft = ""
for _ in range(q):
    t = list(input().split())
    if t[0] == "1":
        rev = not rev
    else:
        f = t[1]
        c = t[2]
        if rev:
            if f == "1":
                aft += c
            else:
                bef += c
        else:
            if f == "1":
                bef += c
            else:
                aft += c
if rev:
    ans = aft[::-1] + s[::-1] + bef
else:
    ans = bef[::-1] + s + aft
print(ans)