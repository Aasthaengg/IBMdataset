s = input()
n = len(s)
t = s.replace("x","")
rt = t[::-1]
m = len(t)
if t != rt:
    print(-1)
    exit()

kouho = [0 for i in range(m+1)]
cou = 0
for i in range(n):
    if s[i] == "x":
        kouho[cou] += 1
    else:
        cou += 1

ans = 0
for j in range(-(-m//2)):
    ans += abs(kouho[j]-kouho[m-j])
    
print(ans)