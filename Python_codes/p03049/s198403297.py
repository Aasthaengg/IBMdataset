n = int(input())
s = [input() for _ in range(n)]


c = 0
ac = 0
bc = 0
abc = 0
for i in range(n):
    c += s[i].count('AB')
    if(s[i][-1] == 'A' and s[i][0] == 'B'):abc += 1
    elif(s[i][-1] == 'A'):ac += 1
    elif(s[i][0] == 'B'):bc += 1

if(abc == 0):
    print(c + min(ac,bc))
elif(ac + bc == 0):
    print(c + abc - 1)
else:
    print(c + abc + min(ac,bc))

