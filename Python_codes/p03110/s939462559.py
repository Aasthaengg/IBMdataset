n = int(input())
ans = 0
for i in range(n):
    s = input().split()
    if s[1]=="JPY":
        ans+=int(s[0])
    elif s[1]=="BTC":
        x = float(s[0])
        ans+=x*380000
print(ans)