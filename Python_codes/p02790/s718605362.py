(a,b) = map(int,input().split())
if a < b:
    l = [str(a)]*b
    print("".join(l))
    

else:
    l = [str(b)]*a
    print("".join(l))