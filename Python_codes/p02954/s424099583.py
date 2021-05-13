def lrCount(rCount,lCount,ansList,i):
    count = rCount + lCount
    c = 0
    if i == len(s) - 1:
        c = 1
    if count % 2 == 0:
        ansList[i - lCount + c] = count // 2
        ansList[i - lCount - 1 + c] = count // 2
    else:
        if rCount % 2 == 1:
            ansList[i - lCount + c] = count // 2
            ansList[i - lCount - 1 + c] = count // 2 + 1
        else:
            ansList[i - lCount + c] = count // 2 + 1
            ansList[i - lCount - 1 + c] = count // 2

import sys

s = input()

if s == "RL":
    print("1 1")
    sys.exit()

check = "N"
ansList = [0 for i in range(len(s))]

for i in range(len(s)):
    if check == "N":
        count = 0
        check = "R"
        rCount = 1
        
    else:
        if s[i] == check and i != len(s) - 1:
            if s[i] == "R":
                rCount += 1
            else:
                lCount += 1
        elif i == len(s) - 1:
            if s[i-1] == "R":
                lCount = 1
            else:
                lCount += 1
            lrCount(rCount,lCount,ansList,i)
        else:
            if s[i] == "L":
                check = "L"
                lCount = 1
            if s[i] == "R":                
                lrCount(rCount,lCount,ansList,i)
                check = "R"
                rCount = 1
                count = 0

for i in range(len(ansList)):
    if i == 0:
        ans = str(ansList[0])
    else:
        ans = ans + " " + str(ansList[i])

print(ans)