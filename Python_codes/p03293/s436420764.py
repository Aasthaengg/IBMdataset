s = input()
t = input()
n = len(s)
for i in range(0,n):
    if s[i:] + s[:i] == t:
        print("Yes")
        quit()
print("No")