r,d,x2000 = map(int,input().split())
x = []
y = 0
for i in range(10):
    y = r*x2000 - d
    x.append(y)
    x2000 = y

for j in range(len(x)):
    print(x[j])