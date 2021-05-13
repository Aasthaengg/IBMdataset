s = list(input())
pee = ""
for i in range(1,len(s)):
    if s[i-1] == "P" and s[i] == "?":
        s[i] = "D"
    if s[i-1] == "?" and s[i] == "D":
        s[i-1] = "P"
    if s[i-1] == "?" and s[i] == "?":
        s[i-1]="P"
        s[i]="D"
for i in range(len(s)):
    if s[i] == "?":
        s[i] = "D"
for i in s:
    pee+=i
print(pee)
