s = str(input())

x = "CODEFESTIVAL2016"
count = 0

for i in range(len(s)):
    if s[i] != x[i]:
        count += 1

print(count)