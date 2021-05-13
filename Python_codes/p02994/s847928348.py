n, l = map(int,input().split())
s = n*l - n + (1+n)*n//2 
if l < 1-n:
    print(s-n-l+1)
elif l <= 0:
    print(s)
else:
    print(s-l)