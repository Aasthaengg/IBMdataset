n = int(input())
#j = L0
j = 2
#k = L1
k = 1

if n == 0:
    print(2)
    exit(0)
if n == 1:
    print(1)
    exit(0)

for i in range(1,n):
    l = j + k
    j = k
    k = l

print(l)