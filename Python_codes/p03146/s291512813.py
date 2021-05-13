s = int(input())
l = []
l.append(s)

count = 1
while True:
    count += 1
    
    n = l[-1]
    if n % 2 == 0:
        a = int(n / 2)
    else:
        a = int(3 * n + 1)
        
    if a in l:
        break
        
    l.append(a)
    
# print(l)
print(count)