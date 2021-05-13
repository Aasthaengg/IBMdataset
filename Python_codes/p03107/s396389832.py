s = str(input())
ze = 0
on = 0
for i in range(len(s)):
    if s[i] == "0":
        ze += 1
    else:
        on += 1
print(len(s)-max(ze,on)+min(ze,on))