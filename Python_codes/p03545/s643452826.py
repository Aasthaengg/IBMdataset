import sys
abcd=str(input())
n=len(abcd)
ans=int(abcd[0])
sign=[]
for i in range(2**(n-1)):
    for j in range(n-1):
        if (i>>j)&1==True:
            ans+=int(abcd[j+1])
            sign.append("+")
        else:
            ans-=int(abcd[j+1])
            sign.append("-")
    if ans==7:
        print(abcd[0]+sign[0]+abcd[1]+sign[1]+abcd[2]+sign[2]+abcd[3]+"=7")
        sys.exit()
    else:
        ans=int(abcd[0])
        sign=[]