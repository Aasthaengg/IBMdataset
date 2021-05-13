n,x,t = map(int,input().split())
m = n//x
if n%x == 0:
    m = m-1
print((m+1)*t)