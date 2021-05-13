N,K = map(int,input().split())

#(ex)K=4
#a%4=1,b%4=2はありえない->なぜならc%4=3かつc%4=2となることはないから
#以上よりa%K = b%K = c%K -> 2つ合わせたらKの倍数より
#mod K で(a,b,c) = (K/2,K/2,K,2) or (a,b,c) = (0,0,0)の2パターンのみ
#1 ~ Nのうち
#1: mod K:K/2 となるものがp個 -> 組み合わせ:p*p*p = p^3通り
#2: mod K:0 となるものがq個 -> 組み合わせ:q*q*q = q^3通り
#ans = p^3 + q^3
p,q = 0,0
if(K%2 == 0):
 for i in range(1,N+1):
  if(i%K == K//2): p += 1
  elif(i%K == 0): q += 1
else:
 for i in range(1,N+1):
  if(i%K == 0): q += 1
ans = p**3 + q**3
print(ans)