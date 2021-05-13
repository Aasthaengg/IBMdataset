n=int(input())
s=''
if n==0:
    print(0)
    exit()
while n!=0:
    m=n%2
    s+=str(m)
    n=(n-m)//-2
print(s[::-1])