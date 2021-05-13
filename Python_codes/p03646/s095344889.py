k = int(input())
n = min(50,k)
if n == k:
    if k >= 2:
        l = [n-1 for i in range(n)]
        l[0] = n
    elif k == 1:
        n = 2
        l = [0,2]
    else:
        n = 2
        l = [0,0]
else:
    a = k//n
    b = k%n
    l = []
    for i in range(n):
        l.append(n-i)
    #print(l)
    for i in range(n):
        l[i] += a-1
    for i in range(b):
        l[i] += 1
print(n)
for i in l:
    print(i,end=" ")