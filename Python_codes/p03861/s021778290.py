a,b,x=map(int,input().split())

a-=1
p=a//x
p*=x

q=b//x
q+=1
q*=x

print((q-p)//x -1)