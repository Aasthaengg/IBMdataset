s = input()
gcount = 0
pcount = 0
vcount = 0
for i in s:
    if i == "p":
        if pcount < gcount:
            pcount+=1
        else:
            gcount+=1
            vcount-=1
    else:
        if pcount < gcount:
            pcount+=1
            vcount+=1
        else:
            gcount+=1
print(vcount)