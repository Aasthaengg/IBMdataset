n, k = map(int,input().split())

ans = 0
#a,b,c = pk,qk,rk
pk = n//k
ans += pk**3

#a,b,c = pk/2,qk/2,rk/2
if k%2 == 0:
    qk = n//(k//2) - pk
    ans += qk**3

print(ans)