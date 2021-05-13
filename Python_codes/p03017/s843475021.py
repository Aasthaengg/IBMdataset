n,a,b,c,d = map(int,input().split())
s = list(input())
for i in range(min(a,b),max(c,d)):
    if s[i] == "#" and s[i+1] == "#":
        print("No")
        quit()
if c < d:
    print("Yes")
elif c > d:
    for j in range(b-1,d):
        if s[j] == "." and s[j+1] == "." and s[j-1] == ".":
            print("Yes")
            quit()
    print("No")