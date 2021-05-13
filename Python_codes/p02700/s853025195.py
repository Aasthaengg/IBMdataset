# 164 B
A,B,C,D = list(map(int, input().split()))
j = 0
while A>0 and C>0:
    j += 1
    C -= B
    if C <= 0:
        break
    j += 1
    A -= D
    
print('Yes') if j%2==1 else print('No')