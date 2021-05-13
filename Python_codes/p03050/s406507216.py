N=int(input())
value=0
if N==1:
    print(0)
    exit()
if N==2:
    print(0)
    exit()
for i in range(1,int(N**.5+10)):
    if N%i==0 and N//i>=i+2:
        value+=N//i-1
print(value)
