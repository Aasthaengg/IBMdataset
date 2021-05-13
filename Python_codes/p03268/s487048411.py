N,K=map(int,input().split())

#a%K=A, b%K=B, c%K=C としたとき,
#A=B=C=0 か、
#A=B=C=K/2 (Kは偶数) のどちらが成り立つ

#N以下のKの倍数の数
kt=N//K

#A=B=C=0を満たす組の数
z=kt*kt*kt

#A=B=C=K/2 (Kは偶数) を満たす組の数
o=0
if K&1==0:
    an=kt+(1 if N%K>=K/2 else 0)
    o=an**3

print(z+o)