n=int(input())
#a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
def f(x,y,z):
    return x**2 + y**2 +z**2 +x*y+y*z+z*x
dic={}
for i in range(1,n+1):
    dic[i]=0
for x in range(1,101):
    for y in range(1,100):
        for z in range(1,100):
            if f(x,y,z)<=n:
                dic[f(x,y,z)]=dic.get(f(x,y,z),0)+1
for i in range(1,n+1):
    print(dic[i])