s = input()
 
n = len(s)
 
ans = 0
 
cunt = 0
 
for i in range(n):
    if s[i] == "B":
        cunt += 1
    else:
        ans += cunt
print(ans)