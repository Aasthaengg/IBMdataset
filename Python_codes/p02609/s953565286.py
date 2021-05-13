def popcount(x):
    return bin(x).count("1")

n=int(input())
s=input()
X=int(s,2)

one_cnt=popcount(X)

modp=X%(one_cnt+1)
modm=X%(one_cnt-1) if one_cnt-1!=0 else 0

for i in range(n):
    if s[i]=="1":
        if one_cnt-1==0:
            print(0)
            continue
        else:
            num=(modm-pow(2,n-i-1,one_cnt-1))%(one_cnt-1)
    else:
        num=(modp+pow(2,n-i-1,one_cnt+1))%(one_cnt+1)

    #print(i,"num",num)
    cnt=1
    while num!=0:
        num=num%popcount(num)
        cnt+=1
    print(cnt)










