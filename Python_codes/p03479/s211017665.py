X,Y=map(int,input().split())

a=X
cnt=0
while a <= Y:
    a=2*a
    cnt+=1


print(cnt)