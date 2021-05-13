strS = input()
strT = input()

strS = list(strS)
strT = list(strT)

maxRange = 0
l = 0
while l <= (len(strS)-len(strT)):
    m = 0
    count = 0
    while m < (len(strT)):
        if strS[l+m] == strT[m]:
            count += 1
        m += 1
    if maxRange < count:
        maxRange = count
    l += 1

print(len(strT)-maxRange)
