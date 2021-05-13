s = input()
q = int(input())
hanten=False
mae=""
usiro=""
for i in range(q):
    tmp=input()
    if len(tmp)==1:
        hanten=not(hanten)
    else:
        if hanten==False:
            if tmp[2]=="1":
                mae=tmp[4]+mae
            else:
                usiro=usiro+tmp[4]
        else:
            if tmp[2]=="1":
                usiro=usiro+tmp[4]
            else:
                mae=tmp[4]+mae
                
ans=mae+s+usiro
if hanten==False:
    print(ans)
else:
    print(ans[::-1])