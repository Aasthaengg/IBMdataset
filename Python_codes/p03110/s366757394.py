n = int(input())

mlis = []
jblis= []
for _ in range(n):
    a, b = input().split()
    mlis.append(float(a))
    jblis.append(b)
    
    
total = 0
for i in range(n):
    if jblis[i] == 'JPY':
        total += mlis[i]
    else:
        total += mlis[i]*380000.0

print(total)