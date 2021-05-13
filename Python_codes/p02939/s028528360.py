s = input()
prev = ""
ans = 0
temp = ""
for i in s:
    temp += i
    if temp == prev:
        pass
    else:
        ans += 1
        prev = temp
        temp = ""
print(ans)