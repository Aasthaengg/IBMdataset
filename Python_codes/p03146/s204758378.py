s = int(input())

a = [s]
idx = 1
n = s
while True:
    if n % 2 == 0:
        n = n // 2
    else:
        n = (3*n) + 1
    idx += 1
    
    if n in a: break
    a.append(n)
    
print(idx)