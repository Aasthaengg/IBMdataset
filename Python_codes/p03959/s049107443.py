n = int(input())
t = [0]+list(map(int,input().split()))+[0]
s = [0]+list(map(int,input().split()))+[0]

mod = 10**9+7
if max(t) != max(s):
    print(0)
    exit()
ans = 1
for i in range(1,n+1):
    d = False
    if t[i] != t[i-1]:
        d = True
        x = t[i]
    if s[i] != s[i+1]:
        if d:
            if x != s[i]:
                print(0)
                exit()
        else:
            d = True
            x = s[i]
    if d:
        if x > t[i] or x > s[i]:
            print(0)
            exit()
    if not d:
        ans *= min(s[i],t[i])
        ans %= mod
print(ans%mod)
