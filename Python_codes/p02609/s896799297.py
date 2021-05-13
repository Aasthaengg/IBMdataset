n=int(input())
x=input()
count_x=x.count("1")
px10=0
nx10=0
xi=[0]*n
ans=[0]*(n+1)
for i in range(1,n+1):
    popcount=format(i,"b").count("1")
    fx=i%popcount
    ans[i]=ans[fx]+1
for i in range(n):
    px10+=(int(x[i])*pow(2,n-1-i,count_x+1))%(count_x+1)
    if count_x!=0 and count_x!=1:
        nx10+=int(x[i])*pow(2,n-1-i,count_x-1)%(count_x-1)
for i in range(n):
    if x[i]=="0":
        xi10=(px10+pow(2,n-1-i,count_x+1))%(count_x+1)
        print(ans[xi10]+1)
    else:
        if count_x!=1:
            xi10=(nx10-pow(2,n-1-i,count_x-1))%(count_x-1)
            print(ans[xi10]+1)
        else:
            print(0)


