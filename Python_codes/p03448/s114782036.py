s = [int(input()) for i in range(4)]
x=0
a=0
b=0
c=0
for i in range(s[0]+1):
    for i in range(s[1]+1):
        for i in range(s[2]+1):
            if 500*a+100*b+50*c == s[3]:
                x=x+1
            c=c+1
        b=b+1
        c=0
    a=a+1
    b=0
    c=0
print(x)