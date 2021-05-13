A = int(input())
B = int(input())
C = int(input())
D = int(input())

train = 0
if A >= B:
    train = B
else :
    train = A
    
bus = 0

if C >= D:
    bus = D
else :
    bus = C
    
print(train+bus)