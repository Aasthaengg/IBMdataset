n = int(input())
a = list(map(int,input().split()))
s,temp = [],0
for i in range(n):
    temp += a[i]
    s.append(temp)
sn,mi = s[n-1],2000000001
for i in range(n-1):
    snuke = s[i]
    arai = sn-s[i]
    if abs(snuke-arai)<mi:
        mi = abs(snuke-arai)
print(mi)