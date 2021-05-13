s = str(input())
start = 0
end = 0
for i in range(len(s)):
    if s[i] == "A":
        start = i
        break

s = s[::-1]


for j in range(len(s)):
    if s[j] == "Z":
        end = len(s) - j
        break

print(end-start)
