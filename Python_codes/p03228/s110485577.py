a, b, k = map(int,input().split())
for i in range(k//2):
    w = a//2
    a = w
    b += w
    w = b//2
    b = w
    a += w
if k%2==1:
    w = a//2
    a = w
    b += w
print(a, b)