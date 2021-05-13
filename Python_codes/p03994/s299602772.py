
s = input()
k = int(input())
n = len(s)

a = []
for i in range(n):
    a.append(ord(s[i])-ord('a'))

for i in range(n):
    need = (26 - a[i])%26
    if(k>=need):
        a[i]=0
        k-=need


k %= 26

for ii in range(n):
    i = n-1-ii
    rem = 25 - a[i]
    if(rem<=k):
        a[i]+=rem
        k-=rem
    else:
        a[i]+=k
        k=0
        
        break
ans = [' ' for i in range(n)]
for i in range(n):        
    ans[i] = chr(a[i]+ord('a'))
print(''.join(map(str,ans)))





