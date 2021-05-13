H = int(input())
SUM = 0
cn = 1

if H == 1:
    print(1)
    exit()

for i in range(10000):
    H = H // 2
    cn = cn + 1
    if H == 1:
        break

for i in range(cn):
    SUM = SUM + (2**i)
    
print(SUM)