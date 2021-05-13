a,b,c=map(str, input().split()) 
if a[len(a)-1:len(a)] == b[0:1] and b[len(b)-1:len(b)] == c[0:1]:
    print("YES")
else:
    print("NO")