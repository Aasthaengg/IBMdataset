N = int(input())
A = list(map(int, input().split()))

cnt = 1
inc = False
dec = False
p = A.pop(0)

for Ai in A:
    if (not inc) and (not dec):
        if Ai < p:
            dec = True
        elif Ai > p:
            inc = True
    elif inc:
        if Ai < p:
            cnt += 1
            inc = False
    elif dec:
        if Ai > p:
            cnt += 1
            dec = False
    p = Ai
    
print(cnt)