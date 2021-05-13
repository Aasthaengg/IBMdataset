S=input()
akh=list("AKIHABARA")
lis=[]
a=[0,4,6,8]
for i in range(16):
    akh=list("AKIHABARA")
    for j in range(4):
        if (i>>j) & 1:
            akh[a[j]]=""
    lis.append("".join(akh))
if S in lis:print("YES")
else:print("NO")