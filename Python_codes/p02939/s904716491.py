s = input()
ans = 0
b = t = ''
for i in s:
    t += i
    if b==t:continue
    ans += 1
    b,t = t,''
print(ans)