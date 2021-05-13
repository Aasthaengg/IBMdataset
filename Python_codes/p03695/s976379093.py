n=int(input())
lst=list(map(int,input().split()))
sp=[]
br=[]
gr=[]
cy=[]
bl=[]
yl=[]
og=[]
rd=[]
colorful=[]

for i in lst:
    if 0<=i<400:
        sp.append(i)
    elif 400<=i<800:
        br.append(i)
    elif 800<=i<1200:
        gr.append(i)
    elif 1200<=i<1600:
        cy.append(i)
    elif 1600<=i<2000:
        bl.append(i)
    elif 2000<=i<2400:
        yl.append(i)
    elif 2400<=i<2800:
        og.append(i)
    elif 2800<=i<3200:
        rd.append(i)
    else:
        colorful.append(i)

if len(colorful)==n:
    print(1,n)
else:
    mi=0
    mx=0
    if len(sp)>0:
        mi+=1
        mx+=1
    if len(br)>0:
        mi+=1
        mx+=1
    if len(gr)>0:
        mi+=1
        mx+=1
    if len(cy)>0:
        mi+=1
        mx+=1
    if len(bl)>0:
        mi+=1
        mx+=1
    if len(yl)>0:
        mi+=1
        mx+=1
    if len(og)>0:
        mi+=1
        mx+=1
    if len(rd)>0:
        mi+=1
        mx+=1
    mx+=len(colorful)
    
    print(mi,mx)