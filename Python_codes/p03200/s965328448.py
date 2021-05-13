s = [a for a in input()]
count = 0
left = 0
for i in range(len(s)):
    if s[i] == "W":
        count += i - left
        left += 1
print(count)