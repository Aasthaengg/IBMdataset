n=int(input())

s=[]
if n%2==0:
    s.append(0)
else:
    s.append(1)
nn=n
ii=0
while nn<=-1 or 2<=nn:
    nn=(nn-s[ii])//(-2)
    if nn%2==0:
        s.append(0)
    else:
        s.append(1)
    ii+=1

ss=""
for i in range(len(s)):
    ss=str(s[i])+ss
print(ss)