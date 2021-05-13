N = int(input())
X = list(map(int, input().split()))
SUM = 0
DIF = 0
for i in range(N):
    SUM = SUM + X[i]

AVG = round((SUM / N))



for i in range(N):
    DIF = DIF + (abs(X[i] - AVG))**2
print(DIF)