N,A,B = map(int,input().split())
onegroup = A+B
syo = N//onegroup
amari = N%onegroup
answer = syo*A + min(amari,A)
print(answer)