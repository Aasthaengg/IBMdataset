n,a,b,c,d = map(int, input().split())
s = list(input())
s.append(".")
a -= 1
b -= 1
c -= 1
d -= 1

if c > d:
    if "##" not in "".join(s[a+1:c]) and "##" not in "".join(s[b+1:d]) and "..." in "".join(s[b-1:d+2]):
        print("Yes")
    else: print("No")
else:
    if "##" not in "".join(s[a+1:c]) and "##" not in "".join(s[b+1:d]):
        print("Yes")
    else: print("No")