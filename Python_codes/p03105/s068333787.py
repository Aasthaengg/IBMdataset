A, B, C = map(int, input().split())

count = 0
A_org = A
A = 0
for i in range(1000):
    if count < C:
        if A + A_org <= B:
            A += A_org
            count += 1
        else:
            break
    else:
        break
    
print(count)