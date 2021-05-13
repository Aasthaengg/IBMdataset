n,a,b=map(int,input().split())
#整数の数はb-a+1
#最小の１つと最大の1つを除いたn-2個について考える
if n==1 and a!=b:
    print(0)
    exit()
elif n==1 and a==b:
    print(1)
    exit()
elif a>b:
    print(0)
    exit()
elif a==b:
    print(1)
    exit()
m=a*(n-2)#最小
M=b*(n-2)#最大
ans=M-m+1
print(ans)