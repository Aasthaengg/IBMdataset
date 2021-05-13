## https://atcoder.jp/contests/abc171/submissions/14626518
## パクった

k=int(input())
s=input()
len_s=len(s)

p = 10 ** 9 + 7

pow26=pow(26,k,p)
pow25=pow(26,p-1-1,p)*25%p 
ans=0
for i in range(k+1): ## i:末尾以外に入る文字数
  ans+=pow26
  ans%=p
  pow26=(pow26*pow25)%p * (len_s+i)%p * pow(i+1,p-2,p)%p
print(ans)