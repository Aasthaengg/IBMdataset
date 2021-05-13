def euclid(m,n):
    while m%n>0:
        m,n=n , m%n
    else:
        return n

x,y = map(int,raw_input().split())
if x < y:
    x,y = y,x
print euclid(x,y)