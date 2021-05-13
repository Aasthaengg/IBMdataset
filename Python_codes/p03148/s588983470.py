Num,K=map(int,input().split())
L=[[]for i in range(Num+1)]
for i in range(Num):
    t,d=map(int,input().split())
    L[t].append(d)
for i in range(1,Num+1):
    L[i].sort(reverse=True)

M=[]
m=[]
for i in range(1,Num+1):
    if len(L[i])>=1:
        M.append(L[i][0])
        if len(L[i])>=2:
            for j in range(1,len(L[i])):
                m.append(L[i][j])
M.sort(reverse=True)
m.sort(reverse=True)
MM=[0]
for i in range(len(M)):
    MM.append(MM[-1]+M[i])
mm=[0]
for i in range(len(m)):
    mm.append(mm[-1]+m[i])
#print(MM)
#print(mm)
ANS=0

def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = 10**9+7 #出力の制限
N = 10**5+10
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

for i in range(1,min(K,len(M))+1):
    ANS=max(i*i+MM[i]+mm[min(len(mm)-1,K-i)],ANS)
    #print(ANS,i)
print(ANS)