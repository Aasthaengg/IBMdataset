a=input().strip().split(" ")

b=[int(i) for i in a]

if(b[1]-b[0]==b[2]-b[1]):
    print("YES")
else:
    print("NO")
