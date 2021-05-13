s = input()
ans = 1000
for i in range(len(s)-2):
    u = abs(eval(s[i]+s[i+1]+s[i+2])-753)
    if u < ans:
        ans = u
print(ans)