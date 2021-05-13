s = list(input())

sc = -1
sf = -1

for i in range(len(s)):
    if s[i] == "C":
        sc = i
    elif s[i] == "F":
        sf = i

if (sc == -1) or (sf == -1):
    print("No")
elif sc < sf:
    print("Yes")
else:
    print("No")
