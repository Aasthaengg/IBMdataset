[a,b,c] = raw_input().split()
a = int(a)
b = int(b)
c = int(c)
k = 0
for t in range(a,b+1):
    if c % t == 0:
        k = k + 1
        
print k