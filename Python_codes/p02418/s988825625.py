s = input()
p = input()
s = s*(len(p)//len(s)+2)

if p in s:
    print("Yes")
else:
    print("No")

