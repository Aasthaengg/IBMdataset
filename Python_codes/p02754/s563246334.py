N, A, B = map(int,input().split())

ans= 0

syo = N // (A+B)
ans+= A*syo

amari = N % (A+B)
if amari >= A:
    ans += A
else:
    ans += amari
print(ans)