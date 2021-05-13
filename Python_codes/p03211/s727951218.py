s = input()
x = list()
for i in range(len(s)-2):
    x.append(int(s[i] + s[i+1] + s[i+2]))
ans = 1000
for j in x:
    ans = min(ans, abs(753-j))    
print(ans)