n, a, b, c, d = map(int, input().split())
a -= 1
b -= 1
c -= 1
d -= 1
s = input()
if c<d:
    if "##" in s[a:c+1] or "##" in s[b:d+1]:
        print("No")
    else:
        print("Yes")
    exit()
else:
    if "##" in s[a:c+1] :
        print("No")
        exit()
    print("Yes" if "..." in s[b-1:d+2] else "No")
