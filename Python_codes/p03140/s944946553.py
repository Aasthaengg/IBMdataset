n=int(input())
a=input()
b=input()
c=input()
x=0
for i in range(n):
    if a[i]==b[i]==c[i]:pass
    elif a[i]==b[i] or b[i]==c[i] or c[i]==a[i]:x+=1
    else:x+=2
print(x)