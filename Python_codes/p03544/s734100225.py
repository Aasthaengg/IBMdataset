N = int(input())
l = 2
l2 = 1

if N == 1:
    print(l2)
    exit()

for i in range(N - 1):
    if i % 2 == 0:
        l = l + l2
    else:
        l2 = l + l2
    
if i % 2 == 1:
    print(l2)
else:
    print(l)