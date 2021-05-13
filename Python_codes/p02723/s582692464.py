ans = "Yes"
s = input()

s = s[2:]

for i in range(2):
    j = 2 * i
    if s[j] != s[j + 1]:
        ans = "No"

print(ans)
