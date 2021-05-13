S = input()
count = 0
passFlag = False
for x in range(len(S)):
    if x == 0:
        count = 1
        prev = S[0]
    else:
        if passFlag:
            passFlag = False
            count += 1
        else:
            if S[x] == prev:
                prev = S[x:x + 2]
                passFlag = True
            else:
                prev = S[x]
                count += 1
print(count)
