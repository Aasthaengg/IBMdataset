s = input()
ans = 0
if (s[0]=='R' and s[1]=='R') and s[2]=='R':
    ans = 3
elif (s[0]=='R' and s[1]=='R')or(s[1]=='R' and s[2]=='R'):
    ans = 2
if ans == 0:
    for i in range(3):
        if s[i]=='R':
            ans = 1
print(ans)
