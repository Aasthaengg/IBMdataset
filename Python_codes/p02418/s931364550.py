s = list(input())
p = list(input())
s += s
for x in range(len(s*2)):
    if p == s[x:x+len(p)]:
        print("Yes")
        break
    else:
        pass
else:
    print("No")


