s=input()
x="KIHBR"
no=[0]
for i in x:
    if not(i in s[no[-1]:]):
        print("NO")
        exit()
    else:
        no.append(s[no[-1]:].index(i)+no[-1])
no.append(len(s))
if no[1]>=2 or no[1]==1 and s[0]!="A" or no[2]-no[1]>=2 or no[3]-no[2]>=2 or no[4]-no[3]>=3 or no[4]-no[3]==2 and s[no[3]+1]!="A" or no[5]-no[4]>=3 or no[5]-no[4]==2 and s[no[4]+1]!="A" or no[6]-no[5]>=3 or no[6]-no[5]==2 and s[no[5]+1]!="A":
    print("NO")
else:
    print("YES")