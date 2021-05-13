s = input()
n = len(s)
rem = 0
ans = 0

for i in range(n):
    if s[i]=="g":
        if rem:
            ans +=1
            rem -=1
        else:
            rem +=1
    else:
        if rem:
            rem -=1
        else:
            ans -=1
            rem +=1
print(ans)