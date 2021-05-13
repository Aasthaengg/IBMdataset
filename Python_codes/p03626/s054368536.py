n = int(input())
s = input()+"0"
s2 = input()##要らない

i = 0

d = []#0が縦、1が横
while i<n:
    try:
        if s[i]==s[i+1]:
            d.append(1)
            i+=1
        else:
            d.append(0)
        i+=1
    except:
        break

ans = 1
#print(d)
if d[0]==0:
    ans = 3
else:
    ans = 6
mod = 10**9+7
for j in range(1,len(d)):
    if d[j]==0:
        if d[j-1]==0:
            ans*=2
    else:
        if d[j-1]==1:
            ans*=3
        else:
            ans*=2####
    ans%=mod
    

    
print(ans)