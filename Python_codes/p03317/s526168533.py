k,n=map(int,input().split())
a=input()
i=0
while True:
    if k<=n+(n-1)*i:print(i+1);break
    i+=1