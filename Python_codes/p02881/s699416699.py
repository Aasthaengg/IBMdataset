
n=int(input())
if int(n**(0.5))==n**(0.5):
    print(2*int(n**0.5)-2)
else:
    m=int(n**(0.5))
    i=m
    while not n%i==0:
        i-=1
    print(i+n//i-2)


    

