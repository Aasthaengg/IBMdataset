s = list(input())
t = list(input())

count = 0
for i in range(len(s)):
    count = count + 1 if s[i] == t[i] else count

print(count)

