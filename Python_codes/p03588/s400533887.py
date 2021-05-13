N = int(input())
MAXA = -1
MINB = -1
for _ in range(N):
    A,B = map(int,input().split())
    if MAXA < A:
        MAXA,MINB = A,B
    
print(MAXA+MINB)