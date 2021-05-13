a=list(input().split())
b=a[0]
a[0]=a[1]
a[1]=b
print("".join(a))