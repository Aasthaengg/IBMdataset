n=int(input())
s=[]
if n==0:
    s.append('0')
while n!=0:
    r=n%(-2)
    if r<0:
        r+=2
    n=(n-r)//(-2)
    s.append(str(r))
s.reverse()
print(''.join(s))
