from collections import Counter
 
h, w = map(int, input().split())
a = Counter(''.join(input() for _ in range(h)))
 
center = h * w % 2 
side = (h//2) * (w%2) + (w//2) * (h%2)
corner = (h//2) * (w//2)

for _ in range(center):
    for i in a:
        if a[i] % 2 == 1:
            a[i] -= 1
            break
for _ in range(side):
    for j in a:
        if a[j] % 4 == 2:
            a[j] -= 2
            break

print('Yes' if sum(a[i]%4 for i in a) == 0 else 'No')
