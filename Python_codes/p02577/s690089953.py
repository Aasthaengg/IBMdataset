o = ['No','Yes']
f = 0
N = str(input())
p = sum(list(map(int,N)))
r = p % 9

if r == 0:
    f = 1
else:
    f = 0

print(o[f])