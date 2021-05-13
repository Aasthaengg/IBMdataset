x = int(input())
v = 100
n = 0
while v < x:
    v += v // 100 
    n += 1
print(n)