n=int(input())
a=[0]*n
for i in range(n):
    a[i]=int(input())
b=sorted(a)
l=len(b)
for i in range(n):
    if a[i]==b[l-1]:
        print(b[l-2])
    else:
        print(b[l-1])