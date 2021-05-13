W, a, b = [int(i) for i in input().split()]

output = 0
if a < b:
    dist = b - (a+W)
    if dist > 0:
        output = dist
else :
    dist = a - (b+W)
    if dist > 0 :
        output = dist
        
print(output)