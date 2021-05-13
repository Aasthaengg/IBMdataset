n, a, b, c, d = map(int,input().split())
s = input()
for i in range(a-1,c-2):
    if s[i] == "#" and s[i+1] == "#":
        print("No")
        exit()
for i in range(b-1,d-2):
    if s[i] == "#" and s[i+1] == "#":
        print("No")
        exit()
if c > d:
    for i in range(b-1,d):
        if s[i] == "." and s[i-1] == "." and s[i+1] == ".":
            print("Yes")
            exit()
    print("No")
else:
    print("Yes")
