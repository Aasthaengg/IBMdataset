x = int(input())
n, d = 0, 100
while d < x:
    d += d // 100 
    n += 1
print(n)