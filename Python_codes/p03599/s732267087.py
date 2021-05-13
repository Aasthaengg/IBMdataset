from operator import itemgetter

A, B, C, D, E, F = list(map(int,input().split()))
X = []
ans = 1000
for i in range(31):
    for j in range(31):
        for k in range(51):
            for l in range(51):
                if 100*A*i+100*B*j+C*k+D*l != 0:
                    if 100*A*i+100*B*j+C*k+D*l <= F and (C*k+D*l)/(100*A*i+100*B*j+C*k+D*l) <= E/(100 + E):
                        ans =(E/(100 + E) - (C*k+D*l)/(100*A*i+100*B*j+C*k+D*l))
                        X.append([ans , 100*A*i+100*B*j+C*k+D*l, C*k+D*l])
X = sorted(X,key=itemgetter(0),reverse = False) 

print(X[0][1],X[0][2])