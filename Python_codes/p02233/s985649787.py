n=int(input())
if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    p=n+1 
    a=((1+5**(1/2))/2)**p
    b=((1-5**(1/2))/2)**p
    c=1/(5**(1/2))
    print(int(c*(a-b)))
