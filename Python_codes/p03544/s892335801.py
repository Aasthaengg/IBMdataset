#47
N = int(input())
l0,l1 = 2,1
l2 = l1
for i in range(N-1):
    l2 = l0 + l1
    l0 = l1
    l1 = l2
    
print(l1)