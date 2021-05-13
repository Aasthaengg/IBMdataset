n,a,b,c,d = map(int,input().split())
s = "s" + input()

for i in range(a,max(c,d)-1):
        if s[i] == s[i+1] == "#":
            print("No")
            exit()
if c < d:
    print("Yes")
else:
    for i in range(b,d+1):
        if s[i+1] == s[i-1] == s[i] == ".":
            print("Yes")
            exit()
    print("No")
