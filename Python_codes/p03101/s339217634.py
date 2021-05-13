A,B=map(int,input().split())
a,b=map(int,input().split())
print((A*B)-(a*b+(A-a)*b+(B-b)*a))