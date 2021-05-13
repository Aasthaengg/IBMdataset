n,a,b,c,d = map(int,input().split())
s = input()
a -= 1
b -= 1
c -= 1
d -= 1

def rockcheck(l,r):
    rock = 0
    for i in range(l,r+1):
        if s[i] == "#":
            rock += 1
            if rock == 2:
                print("No")
                exit()
        else: rock = 0
rockcheck(a,c)
rockcheck(b,d)

ans = "No"
if c < d: ans = "Yes"
else:
    for i in range(b,d+1):
        if s[i] == "#": continue
        if s[i-1] == "." and s[i+1] == ".":
            ans = "Yes"
            break
print(ans)