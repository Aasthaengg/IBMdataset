n=int(input())
#a,b,x=map(int,input().split())
#hl=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())

mn=min(a,b,c,d,e)
print((n+mn-1)//mn +4)
