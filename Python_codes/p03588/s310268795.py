N = int(input())
MAXA = 0
MAXB = 0
for TN in range(0,N):
    A,B = (int(T) for T in input().split())
    if A>MAXA:
        MAXA = A
        MAXB = B
print(MAXA+MAXB)