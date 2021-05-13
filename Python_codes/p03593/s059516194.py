h,w = map(int,input().split())
a = ''

for i in range(h):
    a += input()
from collections import Counter
c = Counter(a)

if h==1 or w==1:
    odd = 0
    for i in c:
        if c[i]%2==1:
            odd += 1
    print('Yes' if odd<=1 else 'No')
    exit()

x = h*(w%2)+w*(h%2)-(h*w)%2
y = 0
z = 0
for i in c:
    y += c[i]%4
    c[i] = c[i]%4
    if c[i]%2==1:
        z += 1

print('Yes' if y<=x and z<=1 else 'No')