a,b,c = map(str,input().split())
a = list(a)
b = list(b)
c = list(c)

if a[-1] == b[0] and b[-1] == c[0]:
    print("YES")
else:
    print("NO")
