s = list(input())
t = list(input())
s.sort()
t.sort(reverse=True)
s = "".join(s)
t = "".join(t)
if t > s:
    print("Yes")
else:
    print("No")