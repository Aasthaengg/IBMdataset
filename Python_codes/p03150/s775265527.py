S = input()

match = "keyence"
check = ""
revcheck = ""

flag = False

for x in range(len(S)):
    if x == len(match):
        break
    if match[x] == S[x]:
        check += S[x]
    else:
        flag = True
        break

if flag:
    remainFlag = False
    remain = match[x:]
    revS = "".join(reversed(S))
    revMatch = "".join(reversed(remain))
    for y in range(len(revS)):
        # print(revS[y])
        if y == len(revMatch):
            remainFlag = True
            break
        if revMatch[y] == revS[y]:
            revcheck += revS[y]
        else:
            break
    if remainFlag:
        print("YES")
    else:
        print("NO")
elif check == match:
    print("YES")
else:
    print("NO")
