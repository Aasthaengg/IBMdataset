a,b,c=input().split()
a1=len(a)
b1=len(b)
if a[a1-1]==b[0] and b[b1-1]==c[0]:
    print("YES")
else:
    print("NO")
