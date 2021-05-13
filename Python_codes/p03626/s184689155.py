import sys
n = int(input())
s = input()
t = []

if (len(s)==1):
    print(3)
    sys.exit()
if (len(s)==2):
    print(6)
    sys.exit()

for i in range(len(s)-1):
    if (i>0):
        if(s[i-1]==s[i]):
            if (i == len(s)-2):
                t.append(1)
                continue
            else:
                continue
        elif (i == len(s)-2 and s[i]!=s[i+1]):
            t.append(1)
            
    
    if (s[i]==s[i+1]):
        t.append(2)
    else:
        t.append(1)

if (t[0]==1):
    ans = 3
else:
    ans = 6

for i in range(len(t)-1):
    
    if (t[i]==1):
        if (t[i+1]==1):
            ans *= 2
        else:
            ans *= 2
    else:
        if (t[i+1]==1):
            ans *= 1
        else:
            ans *= 3
print(ans % 1000000007)