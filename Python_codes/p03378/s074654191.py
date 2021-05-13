N,M,X = map(int, input().split())
li = list(map(int, input().split()))
a = 0
nu = 0
for i in range(1,X):
    if i == li[nu]:
        a += 1
        nu += 1
    if nu == len(li):
        break
b = len(li) - a
if a > b:
    print(b)
else:
    print(a)