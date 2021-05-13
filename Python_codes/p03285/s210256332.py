N = int(input())

max_a = 100 // 4
max_b = 100 // 7
A = False

for a in range(max_a+1):
    if A == True:
        break
    for b in range(max_b+1):
        total = a*4 + b*7
        if total == N:
            A = True
            break
        if total != N:
            A = False
            continue
            
if A == True:
    print('Yes')
if A == False:
    print('No')