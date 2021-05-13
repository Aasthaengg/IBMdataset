s = list(input())
s.sort()
if s.count(s[0]) == 2 and s.count(s[2]) == 2:
    print("Yes")
else:
    print("No")