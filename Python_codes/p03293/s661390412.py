s = input()
t = input()

l = len(s)

for i in range(l):
    temp = s[i:]+s[:i]
    if temp == t:
        print("Yes")
        exit()

print("No")