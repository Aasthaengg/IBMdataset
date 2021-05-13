a=int(input())
b=int(input())
c=int(input())
s=int(input())
n=0
for x in range(a+1):
    for y in range(b+1):
        for z in range(c+1):
            if 500*x+100*y+50*z==s:
                n=n+1
print(n)
