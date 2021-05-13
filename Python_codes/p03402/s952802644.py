a,b = map(int,input().split())

li = []
for _ in range(50):
    li.append(['.'] * 100)
for _ in range(50):
    li.append(['#'] * 100)

for i in range(b-1):
    j = i // 50
    k = i % 50
    li[j*2][k*2] = '#'

for i in range(a-1):
    j = i // 50
    k = i % 50
    li[j*2 + 51][k*2] = '.'

print(100, 100)
for i in range(100):
    for j in range(100):
        print(li[i][j], end = '')
    print()
