a = []
for i in range(3):
    a1, a2, a3 = map(int, input().split())
    a.append(a1)
    a.append(a2)
    a.append(a3)

l = [0]*9
n = int(input())

for i in range(n):
    b = int(input())
    for k in range(9):
        if a[k] == b:
            l[k] += 1
 
if l[0] == 1 and l[1] == 1 and l[2] == 1:
    print('Yes')
elif l[3] == 1 and l[4] == 1 and l[5] == 1:
    print('Yes')
elif l[6] == 1 and l[7] == 1 and l[8] == 1:
    print('Yes')
elif l[0] == 1 and l[3] == 1 and l[6] == 1:
    print('Yes')
elif l[1] == 1 and l[4] == 1 and l[7] == 1:
    print('Yes')
elif l[2] == 1 and l[5] == 1 and l[8] == 1:
    print('Yes')
elif l[0] == 1 and l[4] == 1 and l[8] == 1:
    print('Yes')
elif l[2] == 1 and l[4] == 1 and l[6] == 1:
    print('Yes')
else:
    print('No')