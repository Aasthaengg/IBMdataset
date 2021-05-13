N = int(input())
As = list(map(int, input().split()))
yen = 1000
kabu = 0
for n in range(N-1):
    if As[n] < As[n+1]:
        kabu += yen // As[n]
        yen -= kabu * As[n]
        yen += kabu * As[n+1]
        kabu = 0
print(yen)