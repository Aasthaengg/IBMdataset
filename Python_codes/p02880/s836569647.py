import sys
N=int(input())

a=[]
for i in range(1,10):
    for j in range(1,10):
        a.append(i*j)

for i in range(len(a)):
    if N==a[i]:
        print('Yes')
        sys.exit()
    else:
        continue

print('No')