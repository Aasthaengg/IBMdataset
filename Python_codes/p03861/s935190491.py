a,b,x=map(int,input().split())

q1,r1=divmod(a,x)
q2,_=divmod(b,x)

print(q2-q1+(r1==0))