import collections

N = int(input())
X = []
for i in range(N):
    X.append(list(map(int, input().split())))

div = []
for i in range(N):
    for j in range(N):
        if(i == j):
            continue
        div.append(tuple((X[i][0]-X[j][0], X[i][1]-X[j][1])))
        
c = collections.Counter(div)
c_s = sorted(c.items(), key=lambda x:x[1], reverse=True)

if(N == 1):
    print(1)
else:
    print(N-c_s[0][1])