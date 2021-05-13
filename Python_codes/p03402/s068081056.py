B, A = map(int, input().split())

L = [['.' for i in range(100)] for j in range(100)]

for i in range(100):
    for j in range(100):
        if i >=50:
            L[i][j] = '#'
            
count = 1
now = 0
for i in range(49):
    for j in range(100):
        if count == A:
            break
        if  now%2 == 0 and j%2 == 0:
            L[now][j] = '#'
            count += 1
    now += 1

    if count == A:
        break  
        
count = 1
now = 51
for i in range(51, 100):
    for j in range(100):
        if count == B:
            break
        if  now%2 == 0 and j%2 == 0:
            L[now][j] = '.'
            count += 1

    now += 1
    if count == B:
        break  

print(100, 100)
for i in range(100):
    res = ''
    for j in range(100):
        res += L[i][j]
    print(res)