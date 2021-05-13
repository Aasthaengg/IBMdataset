s = input()
t = input()

for i in range(len(s)):
    if s[i] != t[i]:
        print("No")
        break
    if i == len(s)-1:
        print("Yes")