#\??¨?????????????´???????????????????
RL=[]
#?°´??????????????????????????¨??¢??????????´???????????????????
SL=[]

#\?????????RL????????????????????????????????????
def downer(index):
    RL.append(index)

#/?????????RL??????\????????????????????¢???????¨???????SL???????´?
def upper(index):
    if len(RL) > 0:
        p = RL.pop()
        q = index
        s = q - p
        if len(SL) > 0:
            QL = SL[::-1]
            for i in QL:
                if i[0] > p:
                    s += SL.pop()[1]
                else:
                    break
            SL.append([p, s])
        else: SL.append([p, s])
    else:return

L = input()
index = 0
for i in L:
    if i =="\\":
        downer(index)
        index += 1
    elif i =="/":
        upper(index)
        index += 1
    else:
        index += 1
AL =[]
for i in SL:
    AL.append(i[1])
print(str(sum(AL)))
if len(AL) == 0:
    print(len(AL))
else:
    print(len(AL),end=" ")
    print(" ".join(map(str,AL)))