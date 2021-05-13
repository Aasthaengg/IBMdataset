N = int(input())
s = input()
LWW = 0
LWE = 0
LEW = s[1:].count('W')
LEE = s[1:].count('E')
ans = LWW + LEE
for i in range(1,len(s)):
    if s[i] =="W":
        LEW -=1
    else:
        LEE -=1
    if s[i-1] == 'W':
        LWW +=1
    else:
        LWE +=1
    ans = min(ans,LWW+LEE)
print(ans)    
