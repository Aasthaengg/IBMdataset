N=int(input())
a=len(str(N))#aの桁数
if a==1:
    print(N)
    exit()
else:
    ans=9*(a-1)#Nより1桁少ない値での最大値


    
    for i in range(a):
        y=0
        if i==0:
            for j in range(a):
                y+=int(str(N)[j])
            #print(N)
        else:
            x=str(int(str(N)[:a-i])-1)+"9"*i
            if len(x)!=a:
                x="0"*(a-len(x))+x
            for j in range(a):
                y+=int(x[j])
           # print(x,y)
        if ans<y:
            ans=y
print(ans)