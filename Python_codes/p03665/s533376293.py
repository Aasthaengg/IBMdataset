from math import factorial

n,p = map(int,input().split())
a_input = list(map(int,input().split()))

#p==0:奇数が偶数個になるまで食べる
#p==1:奇数が奇数個になるまで食べる
def calc_comb(n,r):
    return factorial(n) / factorial(r) / factorial(n - r)

odd_len = 0
even_len = 0
for i in range(n):
    if a_input[i]%2==0:
        even_len+=1
    else:
        odd_len+=1

ans=0
even_comb = 2**even_len
if p==0:
    if odd_len%2==0:
        for i in range(0,odd_len+1,2):
            ans+=calc_comb(odd_len,i)*even_comb
    if odd_len%2==1:
        for i in range(1,odd_len+1,2):
            ans+=calc_comb(odd_len,i)*even_comb
else:
    if odd_len%2==0:
        for i in range(1,odd_len+1,2):
            ans+=calc_comb(odd_len,i)*even_comb
    if odd_len%2==1:
        for i in range(0,odd_len+1,2):
            ans+=calc_comb(odd_len,i)*even_comb
print(int(ans))
