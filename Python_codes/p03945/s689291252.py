s = list(input())

if len(set(s)) == 1:
    print(0)
    exit()

ans = 0
tmp = s[0]
state = False
for i in range(1,len(s)):
    if tmp == "B" and s[i] == "W":
        state = True
    elif tmp == "B" and s[i] == "B":
        if state:
            ans += 2
            state = False
            tmp = "B"
    if tmp == "W" and s[i] == "B":
        state = True
    elif tmp == "W" and s[i] == "W":
        if state:
            ans += 2
            state = False
            tmp = "W"

if state:
    ans += 1
print(ans)


