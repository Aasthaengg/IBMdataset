
n = int(input())
X = []
for _ in range(n):
    x = list(map(int, input().split()))
    if x[1] == 0:
        X.append([])
    else:
        X.append(x[2:])
Y = [-1 for _ in range(n)]
def search(i = 0, d = 0):
    if Y[i] > d or Y[i] < 0:
        Y[i] = d
        for x in X[i]:
            search(x - 1, d + 1)
    
search()

for i, y in enumerate(Y):
    print('{} {}'.format(i + 1, y))    

