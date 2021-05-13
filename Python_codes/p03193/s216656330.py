n,h,w = map(int,input().split())
c = 0

for i in range(n):
    a1,b1 = map(int,input().split())
    if (a1 >= h) and  (b1>=w):
        c += 1

print(c)