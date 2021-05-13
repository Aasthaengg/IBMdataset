s = input()
char = [0, 0, 0]
for i in range(len(s)):
    if s[i] == "a":
        char[0] += 1
    elif s[i] == "b":
        char[1] += 1
    else:
        char[2] += 1
char.sort()
char[2] -= char[0]
char[1] -= char[0]
char[0] = 0
if char[1]<=1 and char[2]<=1:
    print("YES")
else:
    print("NO")