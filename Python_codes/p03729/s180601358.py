info=list(input().split())
a=list(info[0])
b=list(info[1])
c=list(info[2])
if a[-1]==b[0] and b[-1]==c[0]:
    print("YES")
else:
    print("NO")