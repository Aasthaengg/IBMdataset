n,l = map(int,input().split(" "))
if l >= 0:
    a = int(((l+1)+(l+n-1))*(n-1)/2)
elif l+n-1 >= 0:
    a = int((l+(l+n-1))*n/2)
else:
    a = int((l+(l+n-2))*(n-1)/2)
print(a)