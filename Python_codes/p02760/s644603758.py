import itertools

a = []
for i in range(3):
    aa = list(map(int,input().split()))
    a.append(aa)
a = list(itertools.chain.from_iterable(a))

b = []
n = int(input())
for i in range(n):
    x = int(input())
    if x in a:
        ii = a.index(x)
        b.append(ii)
c = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]] 
flg = False
for i in range(8):
    ci, cj, ck = c[i][0], c[i][1], c[i][2]
    if ci in b and cj in b and ck in b:
        flg = True
        break
print('Yes') if flg else print('No')