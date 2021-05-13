bai,waru,ama = [int(x) for x in input().split()]
han = "NO"
for i in range(1,10000):
    if bai*i%waru == ama:
        han = "YES"
print(han)