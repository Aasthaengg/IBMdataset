n=int(input())
L=0
R=0

p1=[]
p2=[]
p3=[]

for _ in range(n):

    s=input()

    #パターン１：))((
    #パターン２：))　右に置きたいタイプ
    #パターン３：（（左に置きたいタイプ

    flag=0
    ll=0
    rr=0
    temp=0

    for ss in s:
        if ss==")":
            if  rr>0:
                rr-=1
            else:
                ll+=1
        elif ss=="(":
            rr+=1
 #   print(s,rr,ll)
    if rr>0 and ll>0:
        p1.append((ll-rr,ll,rr))
    elif rr>0:
        p3.append(rr)
    else:
        p2.append(ll)

cnt=0
for item in p3:
    cnt+=item

#print(p1,p2,p3)

p1.sort()
for item in p1:
    lll=item[1]
    rrr=item[2]

    cnt-=lll
    if cnt<0:
        print("No")
        exit()
    cnt+=rrr

    if cnt<0:
        print("No")
        exit()

for item in p2:
    cnt-=item
    if cnt<0:
        print("No")
        exit()
if cnt==0:
    print("Yes")
else:
    print("No")








    



            
