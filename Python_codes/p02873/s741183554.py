s = input()
now = s[0]
c = []
count = 1
for i in range(1,len(s)):
    if (now == s[i]):
        count += 1
    else:
        c.append(count)
        now = s[i]
        count = 1
c.append(count)
#print(c)

def ta(n):
    ans = 0
    for i in range(1,n+1):
        ans += i
    return ans

if (s[0] == "<"):
    a = []
    for i in range(len(c)//2):
        a.append(max(c[2*i],c[2*i+1]))
        a.append(min(c[2*i],c[2*i+1])-1)
    if (len(c)%2==1):
        a.append(c[-1])
    #print(a)
    ans = 0
    for i in a:
        ans += ta(i)
    print(ans)
else:
    a = []
    a.append(c[0])
    for i in range((len(c)-1)//2):
        a.append(max(c[2*i+1],c[2*i+2]))
        a.append(min(c[2*i+1],c[2*i+2])-1)
    if (len(c)%2==0):
        a.append(c[-1])
    ans = 0
    for i in a:
        ans += ta(i)
    print(ans)