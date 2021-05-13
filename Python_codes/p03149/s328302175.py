line = input().split()
d = {}
for i in line:
    d[i] = True

if "1" in d and "9" in d and "7" in d and "4" in d:
    print("YES")
else:
    print("NO")