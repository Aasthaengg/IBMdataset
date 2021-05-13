a=input()
b=0
c=len(a)//2
for i in range(c-1):
    if a[0:i]==a[i+1:i+1+i]:
        b=i+1
print(b*2)
