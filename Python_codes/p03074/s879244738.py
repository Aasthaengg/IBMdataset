n,k = map(int,input().split())
s = input()
al = []

a0 = 1
    
for i in range(n-1):
    if s[i] != s[i+1]:
        al.append(a0)
        a0 = 1
    else:
        a0 += 1
        
al.append(a0)

if s[0] == "0":
    al = [0] + al
if s[-1] == "0":
    al = al + [0]
    
nn = len(al)
nagasa = min(2*k+1,nn)
r = (nn-nagasa) // 2

ans = sum(al[:nagasa])
cur = sum(al[:nagasa])
for i in range(1,r+1):
    cur = cur + (al[nagasa+i*2-1] + al[nagasa+i*2-2]) -(al[i*2-1] + al[i*2-2])
    ans = max(cur,ans)
    
print(ans)