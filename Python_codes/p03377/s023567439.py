A,B,X = map(int,input().split())

if X < A:
    print("NO")
    exit()
    
if (A+B) < X:
    print("NO")
else:
    print("YES")
