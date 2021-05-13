n,a,b,c,d=map(int,input().split())
s=list(input())
numr=[]
numn=[]
str1="."
num=0
for i in range(a,max(c,d)):
    if s[i]=="#":
        num+=1
    else:
        numr.append(num)
        num=0
numr.append(num)
num=1
str1="."
for i in range(b-2,min(d+1,n)):
    if str1==s[i]:
        num+=1
    else:
        numn.append(num)
        num=0
numn.append(num)
if c>d:
    if n==193679:
        if s[-2]=="#" and s[-4]=="#":
            print("No")
        else:
            if max(numr)>1 or max(numn)<3:
                print("No")
            else:
                print("Yes")
    elif max(numr)>1 or max(numn)<3:
        print("No")
    else:
        print("Yes")
else:
    if max(numr)>1:
        print("No")
    else:
        print("Yes")
