N,A,B = map(int,input().split())

AB = A+B

shou = N//AB

amari = N%AB

ans = shou*A+min(A,amari)

print(ans)