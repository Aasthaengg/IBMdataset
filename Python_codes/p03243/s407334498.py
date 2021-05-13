n=int(input())
if n%111==0:
    print(n)
else:
    x=n//111
    print((x+1)*111)