a,b=map(int,input().split())
A=[str(a)*b]
B=[str(b)*a]
if a>b:
    print(int(''.join(B)))
if a<b:
    print(int(''.join(A)))
if a==b:
    print(int(''.join(A)))