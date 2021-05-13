n = int(input())
s = input()
s1 = []
mod = 1000000007
i = 0
while i < n-1:
    if s[i]==s[i+1]:
        s1.append(0)
        i += 1
    else:
        s1.append(1)
    i += 1

if s[n-2]!=s[n-1]:
    s1.append(1)

if n==1:
    s1.append(1)

ans = 1
for i in range(len(s1)):
    ans %= mod
    if i == 0:
        if s1[i]==0:
            ans*=6
        else:
            ans*=3
    elif s1[i-1]==0 and s1[i]==0:
        ans*=3
    elif s1[i-1]==1 and s1[i]==1:
        ans*=2
    elif s1[i-1]==1 and s1[i]==0:
        ans*=2

print(ans%mod)