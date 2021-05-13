icase=0    
if icase==0:
    a,b,c=map(int,input().split())
    if b-a==c-b:
        print("YES")
    else:
        print("NO")