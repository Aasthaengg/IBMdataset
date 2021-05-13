n = int(input())
a = 0
b = 0
c = 0
ans = 0
for _ in range(n):
    s = input()
    if s[0]=='B' and s[-1]=='A':
        c+=1
    elif s[0]=='B':
        b+=1
    elif s[-1]=='A':
        a+=1
    
    for i in range(len(s)-1):
        if s[i:i+2] == 'AB':
            ans += 1
if c>0:
    ans += c-1
    if b>0:a += 1
    if a>0:b += 1

ans += min(a,b)
print(ans)