def sum(a):
    c=0
    if a%2==0:
        n=a//2
    else:
        n=a//2+1
    for i in range(1,n):
        if a-i<a and a-i>=1:
            c=c+1
    return c
a=int(input())
print(sum(a))

