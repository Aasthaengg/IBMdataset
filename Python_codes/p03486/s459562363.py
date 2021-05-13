s = input()
t = input()
s1 = sorted(s)
t1 = sorted(t, reverse=True)
if s1 < t1:
    print("Yes")
else:
    print("No")