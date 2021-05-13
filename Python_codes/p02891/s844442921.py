s=input()
k=int(input())
n = len(s)
same = True
for i in range(1,len(s)):
    if s[i]!=s[i-1]:
        same = False
if same:
    print(len(s)*k//2)
    exit()

for i in range(1,len(s)):
    if s[i] != s[i-1]:
        before = i-1
        break
for i in range(len(s)-1,-1,-1):
    if s[i] != s[i-1]:
        after = i
        break

ans = (before+1)//2 
ans += (len(s)-after)//2
if s[0] == s[-1]:
    ans += (before + 1 + len(s) - after)//2 * (k-1)
else:
    ans += ((before+1)//2  + (len(s)-after)//2)*(k-1)
cnt = 1
for i in range(before+2, after):
    if s[i] != s[i-1]:
        ans += cnt //2 *k
        cnt = 1
    else:
        cnt +=1
ans += cnt //2 * k
print(ans)
