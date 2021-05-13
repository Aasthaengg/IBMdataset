h=int(input())
s=0
while h>1:
    h=h//2
    s=s+1
else:
    h=1
x=0
for i in range(s+1):
    x+=2**i
print(x)