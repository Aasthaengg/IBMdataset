def popcount(x):
    return bin(x).count("1")


n=int(input())
x=input()
num=int(x,2)
cnt=popcount(num)

mod1=num%(cnt+1)
mod2=num%(cnt-1) if cnt-1!=0 else 0

for i in range(n):
    if x[i]=="0":
        ans=(mod1+pow(2,n-i-1,cnt+1))%(cnt+1)
    else:
        if cnt-1==0:
            print(0)
            continue
        else:
            ans=(mod2-pow(2,n-i-1,cnt-1))%(cnt-1)
    point=1
    while ans!=0:
        ans %=popcount(ans)
        point +=1
    print(point)