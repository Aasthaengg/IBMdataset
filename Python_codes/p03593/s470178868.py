from collections import Counter
H,W = map(int,input().split())
A = [input() for i in range(H)]
ctr = Counter()
for row in A:
    ctr.update(row)

if H%2==0 and W%2==0:
    print('Yes' if all(v%4==0 for v in ctr.values()) else 'No')
    exit()

if H%2 and W%2:
    for k,v in ctr.items():
        if v%2:
            ctr[k] -= 1
            break
if any(v%2 for v in ctr.values()):
    print('No')
    exit()

if H%2 and W%2:
    two = W+H-1
elif H%2:
    two = W
else:
    two = H

for k,v in ctr.items():
    if v%4==0: continue
    if two <= 0:
        print('No')
        exit()
    two -= 2

print('No' if two%4==2 else 'Yes')