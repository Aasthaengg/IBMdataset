x = ["".join(sorted(input()))]
x.append("".join(sorted(input())[::-1]))
s = x[0]
x.sort()
if x[0]==x[1]:
    print("No")
    exit()
print("Yes" if s == x[0] else "No")