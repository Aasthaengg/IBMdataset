s=input()
p="AKIHABARA"
c=[0,4,6,8]
for i in range(16):
    t=bin(i)[2:]
    t="0"*(4-len(t))+t
    d=p[:]
    for j in range(4):
        if t[j]!="1":
            d=d[:c[j]]+"?"+d[c[j]+1:]
    else:
        if d.replace("?","")==s:
            print("YES")
            break
else:
    print("NO")