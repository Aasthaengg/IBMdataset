n=int(input())
s=input()
t=input()
c=0
for i in range(n):
    moji=n-i
    a=s[-moji:]
    b=t[:moji]
    if a==b:
        c=n-i
        break
print(2*n-c)