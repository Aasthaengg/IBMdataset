n,*a=open(0).read().split()
ba=xa=bx=ans=0
for i in a:
    if i[0]=="B" and i[-1]=="A":
        ba+=1
    elif i[0]=="B":
        bx+=1
    elif i[-1]=="A":
        xa+=1
    ans+=i.count("AB")    
print(ans+min(xa,bx)+ba-1*(ba>0 and xa==bx==0))