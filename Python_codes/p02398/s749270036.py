r = 0
a,b,c = [int(i) for i in input().split()]
for i in range((b + 1) - a):
    t = c % a
    if(t == 0):
        r += 1
    a += 1
print(r)