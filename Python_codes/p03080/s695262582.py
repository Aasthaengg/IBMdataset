N = int(input())
s = input()

red = 0
blue=0
for c in s:
    if c=='R':
        red+=1
    else:
        blue+=1

if red>blue:
    print("Yes")
else:
    print("No")