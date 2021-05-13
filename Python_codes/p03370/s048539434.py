N,X=map(int,input().split())
D=[]
num=0
for i in range(N):
    m=int(input())
    D.append(m)
    X-=m
    if X<min(D):
        print(N)
        exit()
while X>=min(D):
    X-=min(D)
    num+=1
    if X<min(D):
        print(N+num)
        exit()
