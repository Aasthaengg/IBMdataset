import sys
s = input()
for i in range(8):
    siki = s[0]
    tmp = int(s[0])
    for j in range(3):
        if i&(1<<j):
            siki = siki+'+'+s[j+1]
            tmp+=int(s[j+1])
        else:
            siki = siki + '-' + s[j+1]
            tmp-=int(s[j+1])
    if tmp==7:
        print(siki,"=7",sep="")
        exit()