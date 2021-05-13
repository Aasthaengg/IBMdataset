n = int(input())
a = list(map(int,input().split()))
m2 = 0
m4 = 0
other=0
for i, aa in enumerate(a):
    if aa % 4 == 0:
        m4 +=1
        continue
    if aa % 2 == 0:
        m2 += 1
        continue
    other += 1
if m4 >= other or (m4 + 1 == other and m2 == 0):
    print('Yes')
else:
    print('No')
