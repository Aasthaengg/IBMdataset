n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
pdiff = 0
ndiff = []
for i, j in zip(a, b):
    if i-j>0:
        pdiff += i-j
    elif i-j<0:
        ndiff.append(j-i)

while ndiff:
    tmp = ndiff.pop()
    pdiff -= tmp//2
if pdiff<=0:
    print('Yes')
else:
    print('No')