N = int(input())
T = [0]
X = [0]
Y = [0]
for i in range(N):
    t,x,y = map(int,input().split())
    T.append(t)
    X.append(x)
    Y.append(y)

flag = True
for i in range(N):
    time = T[i+1]-T[i]
    dist = abs(X[i+1]-X[i])+abs(Y[i+1]-Y[i])
    if time < dist or (dist%2!=time%2):
        flag = False
        break
if flag:
    print('Yes')
else:
    print('No')
