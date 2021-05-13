word = str(input())
wlist = []
for i in word:
    wlist.append(i)
n = int(input())
for i in range(n):
    com = list(input().split())
    a = int(com[1])
    b = int(com[2])
    if (com[0] == 'print'):
        for k in range(a, b + 1):
            print(wlist[k], end ='')
        print()
    elif (com[0] == 'reverse'):
        decoy = []
        for k in range(a, b+1):
            decoy.append(wlist[b+a-k])
        for l in range(b-a+1):
            wlist[a+l] = decoy[l]
    elif (com[0] == 'replace'):
        p = str(com[3])
        plist = []
        for k in p:
            plist.append(k)
        for l in range(b-a+1):
            wlist[a+l] = plist[l]
            
