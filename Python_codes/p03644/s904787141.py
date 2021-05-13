n = int(input())
l = []

for i in range(n+1):
    if 2**i <= n:
        l.append(2**i)
    
print(max(l))