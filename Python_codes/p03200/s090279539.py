s = str(input())
l = list(s)
b = l.count("B")
w = l.count("W")
ans = 0
counter = 0
for i in range(len(l)):
    if l[i] == "W":
        ans += (i - counter)
        counter += 1
print(ans)