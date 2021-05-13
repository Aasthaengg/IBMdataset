c = input()
s = input()
cl = list(c)
sl = list(s)

cr = list(reversed(cl))

if sl == cr:
    print("YES")

else:
    print("NO")