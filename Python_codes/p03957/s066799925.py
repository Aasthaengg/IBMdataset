s = list(input())

c = -1
f = -1

for i in range(len(s)):
    if s[i] == "C" and c == -1:
        c = i
    if s[i] == "F":
        f = i
        
if c < f and c != -1:
    print("Yes")
else:
    print("No")