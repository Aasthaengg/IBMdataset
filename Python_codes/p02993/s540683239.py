s = list(input())
ans = 1
for i in range(4-1):
    if s[i] == s[i+1]:
        ans = 0
print(["Bad","Good"][ans])
