n = int(input())
s = input()
t = input()
duplicates = 0
for i in range(n):
    if s[-(i + 1):] == t[:i + 1]:
        duplicates = i + 1
temp = s + t[duplicates:]
print(len(temp)) 