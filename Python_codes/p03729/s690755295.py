a,b,c=(input().split())
alen=len(a)
blen=len(b)
clen=len(c)
if a[int(alen)-1]==b[0] and b[int(blen)-1]==c[0]:
    print("YES")
else:
    print("NO")