n=int(input())
x_=input()
px=x_.count("1")
if not px:
    for i in range(n):
        print(1)
    exit()
if px==1:
####[上から] i 桁目
    for i in range(n):
        if int(x_[i]):
            print(0)
        else:
            if i==n-1 or int(x_[-1])==1:###
                print(2)
            else:
                print(1)
    exit()
x=int(x_,2)

pow2=[1]

for i in range(n):
    tmp=pow2[-1]
    tmp*=2
    tmp%=px+1
    pow2.append(tmp)
pow22=[1]
for i in range(n):
    tmp=pow22[-1]
    tmp*=2
    tmp%=px-1
    pow22.append(tmp)
x1=x%(px+1)
x2=x%(px-1)
ans=[]
for i in range(n):
    tmp=0;dv=0
    if int(x_[-i-1]):
        tmp=x2-pow22[i]
        tmp%=(px-1)
        dv=px-1
    else:
        tmp=x1+pow2[i]
        tmp%=(px+1)
        dv=px+1
    
    cnt=1
    while tmp:
        
        dv=bin(tmp).count("1")
        if not dv or not tmp:
            break
        
        tmp%=dv
        cnt+=1
    ans.append(cnt)
for i in ans[::-1]:
    print(i)
