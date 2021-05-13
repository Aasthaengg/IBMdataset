s = input()
t = input()

# s' < t'にできるか?
ss = sorted(s)
tt = sorted(t, reverse=True)

if ss < tt:
    print("Yes")
else:
    print("No")
