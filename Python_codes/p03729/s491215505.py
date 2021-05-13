icase=0    
if icase==0:
    a,b,c=input().split()
    if a[-1]==b[0] and b[-1]==c[0]:
        print("YES")
    else:
        print("NO")