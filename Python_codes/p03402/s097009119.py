A,B = map(int,input().split())
s1 = [['#']*100 for _ in range(50)]
s2 = [['.']*100 for _ in range(50)]

A -= 1
B -= 1
for i in range(50):
    for j in range(100):
        if A == 0:
            break
        if i%2==0 and j%2==0:
            s1[i][j] = '.'
            A -= 1
for i in range(50):
    for j in range(100):
        if B == 0:
            break
        if i%2==1 and j%2==1:
            s2[i][j] = '#'
            B -= 1

S = [''.join(s) for s in s1]+[''.join(s) for s in s2]
print('100 100')
for s in S:
    print(s)