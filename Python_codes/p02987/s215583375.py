a = list(input())
a.sort()
if a.count(a[0]) == 2 and a.count(a[-1]) == 2:
    print("Yes")
else:
    print("No")