import math

#成績xを取れるか？xに関して二分探索

N,K = map(int,input().split())
A = list(map(int,input().split()))
F = list(map(int,input().split()))

#Aを小さい順，Fを大きい順に並べれば対応する．
A.sort()
F.sort(reverse =True)
AF=[0]*N

for i in range(N):
    AF[i]=A[i]*F[i]
    
ng=-1
ok=10**12+1

#二分探索，成績xをとるのにi番目の人が何回修行すべきか，これがK以下なら良い
while ok-ng!=1:
    x = (ok+ng)//2
    num_tra =0
    for i in range(N):
        af_i = int(math.ceil((AF[i]-x)/F[i]))
        if af_i>0:
            num_tra+=af_i
    if num_tra<=K:
        ok=x
    else:
        ng=x
        
print(ok)