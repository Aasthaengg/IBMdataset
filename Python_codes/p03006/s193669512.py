from collections import Counter
N = int(input())
X = []
for i in range(N):
    x,y = map(int,input().split())
    X.append((x,y))
kouho = []
for i in range(N):
    for j in range(N):
        if i==j:continue
        kouho.append((X[i][0]-X[j][0],X[i][1]-X[j][1]))
C = Counter(kouho)
if len(C)==0:print(1)
else:print(N-max(C.values()))