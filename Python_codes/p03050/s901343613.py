#n//m=kかつn%m=kはつまりn=k(m+1)、また、k<m

n=int(input())

sq = int(n**(1/2))+2
ans = 0
for i in range(1,sq):
    if n%i==0:
        j = n//i-1
        if j:#nが小さいと0になる？
            if n//j==n%j:#境界処理が面倒なので試す
                ans +=j

print(ans)

