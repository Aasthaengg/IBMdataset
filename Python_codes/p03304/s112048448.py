import sys 
n,m,d=map(int,input().split())
if d==0:
    print( (m-1)/n)
    sys.exit()
print(((m-1)*2*(n-d))/(n*n)) 