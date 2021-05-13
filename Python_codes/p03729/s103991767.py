li=input().split()
a=li[0]
b=li[1]
c=li[2]
if a[-1:-2:-1]==b[0:1] and b[-1:-2:-1]==c[0:1]:
    print("YES")
else:
    print("NO")
