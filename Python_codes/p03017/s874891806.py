n,a,b,c,d = [int(x) for x in input().split()]
s = input()

if s[a-1:c].count("##") > 0 or s[a-1:d].count("##") > 0:
    print("No")
elif d < c:
    if s[b-2:d+1].count("..."):
        print("Yes")
    else:
        print("No")
else:
    print("Yes")