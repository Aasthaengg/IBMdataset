s = input()
n = len(s)
if n == 7:
    if s == "keyence":
        print("YES")
    else:
        print("NO")
else:
    if s[n-7:n] == "keyence" or (s[0]+s[n-6:n]) == "keyence" or (s[0:2]+s[n-5:n]) == "keyence" or (s[0:3]+s[n-4:n]) == "keyence" or (s[0:4]+s[n-3:n]) == "keyence" or (s[0:5]+s[n-2:n]) == "keyence" or  (s[0:6]+s[n-1:n]) == "keyence"  or (s[0:7]) == "keyence":
        print("YES")
    else:
        print("NO")