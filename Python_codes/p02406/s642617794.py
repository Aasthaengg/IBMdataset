n = int(input())
s = ''
for i in range(1, n + 1):
    if i % 3 == 0:
        s += ' %d' % i
        continue
    
    j = i
    while j != 0:
        if j % 10 == 3:
            s += ' %d' % i
            break
        j = j // 10
    
print(s)