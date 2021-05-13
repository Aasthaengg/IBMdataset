abc=list(map(int,input().split()))
a,b,c=abc[0],abc[1],abc[2]
k=int(input())
for i in range(k+1):
    if a < b < c:
        print("Yes")
        break
    elif b <= a < c:
        b *= 2
    else:
        c *= 2
else:
    print("No")