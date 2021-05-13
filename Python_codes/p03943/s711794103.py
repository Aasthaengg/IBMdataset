mylist = list(map(int, input().split()))
s = sorted(mylist)
if s[0] + s[1] == s[2]:
    print("Yes")
else:
    print("No")