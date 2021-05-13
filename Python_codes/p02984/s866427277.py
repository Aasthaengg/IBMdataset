n = int(input())
a = list(map(int,input().split()))
x0 = 0
for i in range(n):
    x0 += a[i]*(-1)**(i)
print(x0,end="")
print(" ",end="")
x = x0//2
for i in range(1,n):
    x = a[i-1] - x
    print(2*x,end="")
    print(" ",end="")
print("")