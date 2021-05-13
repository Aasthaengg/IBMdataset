s = input()
ca,cb,cc = 0,0,0
for i in range(len(s)):
    if s[i] == "a":
        ca += 1
    elif s[i] == "b":
        cb += 1
    else:
        cc += 1
mx = max(max(ca,cb),cc)
mn = min(min(ca,cb),cc)
if mx - mn >= 2:
    print("NO")
else:
    print("YES")