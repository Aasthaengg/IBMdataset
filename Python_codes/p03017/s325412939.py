[n,a,b,c,d] = [int(i)-1 for i in input().split()]
s = input()
if c < b:
    if "##" in s[a:c+1] or "##" in s[b:d+1]:
        print("No")
    else:
        print("Yes")
elif d < c :
    if "##" not in s[a:c+1]and "..." in s[b-1:d+2]:
        print("Yes")
    else:
        print("No")
else:
    if "##" not in s[b:d+1]:
        if "##" not in s[a:c+1]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
