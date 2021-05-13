a,b,c = map(int,input().split(" "))

if a < b and a < c:
    if b < c:
        print("Yes")
else:
    print("No")