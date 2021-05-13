r,d,x = map(int,input().split())
l = []

s = x
for i in range(10):
    s = s * r - d
    l.append(str(s))

ans="\n".join(l)
print(ans)