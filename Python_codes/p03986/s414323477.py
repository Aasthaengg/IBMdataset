s=input()
ans=0
i=0
c=-1
tmp1=0#Sが連続した数
tmp2=0
x=0
y=0
while i<len(s):
    if c==-1:
        if s[i]=="S":
            tmp1=1
            c=0
        else:
            tmp2+=1
            c=1
    elif c==0:
        if s[i]=="S":
            tmp1+=1
        else:
            tmp2+=1
            c=1
    elif c==1:
        if s[i]=="S":
            if tmp1>=tmp2:
                tmp1=tmp1-tmp2
                tmp2=0
            else:
                y+=tmp2-tmp1
                tmp2=0
                tmp1=0
            c=0
            tmp1+=1
        else:
            tmp2+=1
    if i==len(s)-1:
        if tmp1>=tmp2:
            x+=tmp1-tmp2
            tmp2=0
        else:
            y+=tmp2-tmp1
            tmp1=0
    i+=1
    
    #print(ans,tmp1,tmp2,x,y)
print(x+y)