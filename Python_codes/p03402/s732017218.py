a,b = map(int,input().split())
k = 50
d = [['.' if i<k else '#' for j in range(2*k)] for i in range(2*k)]
a-=1
b-=1
for i in range(0,50,2):
    for j in range(0,100,2):
        if b>0:
            d[i][j] = '#'
            b-=1

for i in range(51,100,2):
    for j in range(0,100,2):
        if a>0:
            d[i][j] = '.'
            a-=1

print(2*k, 2*k)
for s in d:
    print("".join(s))
