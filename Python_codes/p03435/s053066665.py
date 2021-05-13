import sys
c = []

for _ in range(3):
    c += [list(map(int, input().split()))]

a = [0, -1, -1]
b = c[0]

for l, m in enumerate(c[1:]):
    for j, k in enumerate(m):
        if j == 0:
            a[l+1] = k - b[j] 
        else:
            if k != a[l+1] + b[j]:
                print('No')
                sys.exit()
print('Yes')
    

