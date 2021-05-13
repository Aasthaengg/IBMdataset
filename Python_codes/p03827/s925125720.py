a = [input() for i in range(2)]
result = int(0)
maxAns = int(0)
for c in a[1]:
    if c == 'I':
        result += 1
    elif c == 'D':
        result -= 1
    
    if result > maxAns:
        maxAns = result

print(maxAns)