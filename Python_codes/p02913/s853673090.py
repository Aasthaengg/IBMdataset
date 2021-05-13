n = int(input())
s = input()
#長さnの文字列s
def gene_hash(i,j): #特定範囲のハッシュを返す s[i:j]
    return (hash1[j]-hash1[i]*power1[j-i]%mod1)%mod1

base1 = 1007
mod1 = 10**9+7

hash1 = [0]*(n+1)
power1 = [1]*(n+1)

for i,e in enumerate(s):
    hash1[i+1] = (hash1[i]*base1 + ord(e))%mod1
    power1[i+1] = (power1[i]*base1)%mod1
    
lef = 0
rig = n//2 + 1

while rig - lef > 1:
    mid = (rig+lef)//2
    Flag = False
    for i in range(n-2*mid+1):
        if Flag:
            break
        now = gene_hash(i,i+mid)
        for j in range(i+mid,n-mid+1):
            if now == gene_hash(j,j+mid):
                Flag = True
                break
    if Flag:
        lef = mid
    else:
        rig = mid
print(lef)