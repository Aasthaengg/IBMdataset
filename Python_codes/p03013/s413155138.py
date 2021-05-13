def Fib(n):
    a, b = 1, 1
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        for i in range(n-2):
            a, b = b, a + b
        return b

n,m = map(int,input().split())
a = [int(input()) for _ in range(m)]

for i in range(len(a)-1):
    if a[i+1] == a[i]+1:
        print(0)
        exit()
x = []
temp=0
for i in range(m):
    x.append(a[i]-temp-1)
    temp = a[i]+1
x.append(n-temp)

temp = 1
div = 1000000007

for i in x:
    temp = (temp*Fib(i+1))%div

print(temp)