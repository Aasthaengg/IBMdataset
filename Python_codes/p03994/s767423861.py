s=input()
k=int(input())
ls=[]
lord=[]
for i in range(len(s)):
    ls.append(s[i])
    lord.append(ord(s[i]))
i=0
while k>0 and i<len(s):#z的码值为122，再变成a，次数需要增加1，则123。
    if lord[i]!=97 and k>=123-lord[i]:    #如原本为a,则不变
        k=k-(123-lord[i])
        lord[i]=97
        ls[i]='a'
    i+=1

if k>0:
    lord[-1]=lord[-1]+k%26
    ls[-1]=chr(lord[-1])
for x in ls:
    print(x,end="")




