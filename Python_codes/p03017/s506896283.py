n,a,b,c,d = map(int,input().split())
a -= 1
b -= 1
c -= 1
d -= 1
s = input()
for i in range(a,c+1):
    if s[i] == "#":
        if s[i-1] == "#":
            print("No")
            exit()
for i in range(b,d+1):
    if s[i] == "#":
        if s[i-1] == "#":
            print("No")
            exit()
if (a > b and c > d) or (a < b and c < d):
    print("Yes")
else:
    for i in range(max(a,b),min(c,d)):
        if i == b:
            if s[i-1] == "." and s[i+1] == ".":
                break
        if s[i] == "." and s[i+1] == "." and s[i+2] == ".":
            break
    else:
        print("No")
        exit()
    print("Yes")
