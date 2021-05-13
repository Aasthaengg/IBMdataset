A="AKIHABARA"
data=[0,4,6,8]
AD=list(A)
S=set(); S.add(A)
for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                tmp=AD.copy()
                # print(AD)
                # print(tmp)
                if i: tmp[0]=""
                if j: tmp[4]=""
                if k: tmp[6]=""
                if l: tmp[8]=""
                S.add(''.join(tmp))


s=input()
if s in S:
    print("YES")
else:
    print("NO")