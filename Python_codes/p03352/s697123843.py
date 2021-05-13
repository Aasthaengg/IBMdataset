x = int(input())

beki = {1}
for b in range(2,32):
    for p in range(2,10):
        if b**p<=x:
            beki.add(b**p)
        else:
            break
            
beki = sorted(beki)
            
print(beki.pop(-1))