N, X = map(int, input().split())
m = [int(input()) for i in range(N)]


SUM = 0

for i in range(N):
    SUM = SUM + m[i]
    

    
Z = X - SUM


MIN = min(m)


ANS = Z // MIN

print(ANS + N)