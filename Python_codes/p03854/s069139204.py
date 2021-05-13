s = input()
l = len(s)

idx = 0
ans = "NO"
dream = False
erase = False
while idx<l:
    if s[idx]=="d":
        if s[idx:(idx+5)] == "dream":
            idx += 5
            dream = True
            erase = False
        else:
            break
    elif s[idx] == "e":
        if s[idx+1] != "r":
            break
        else:
            if s[idx:(idx+5)] == "erase":
                idx += 5
                erase = True
                dream = False
            elif dream:
                idx += 2
                erase = False
                dream = False
            else:
                break
    elif s[idx]== "r":
        if erase:
            idx += 1
            erase = False
            dream = False
        else:
            break
    else:
        break

if idx == l:
    ans = "YES"

print(ans)