n = int(input())
N = 10**9
x1=0
y1=0
x2=N
y2=1
x3=N-n%N
y3=n//N+1
if n==10**18:
    x3=0
    y3=n//N

print(x1,y1,x2,y2,x3,y3)
