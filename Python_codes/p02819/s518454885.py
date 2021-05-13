P = [1 for _ in range(10**6)]
P[0]=0
P[1]=0
for i in range(2,10**3+1):
    for j in range(i*i,10**6,i):
        P[j]=0
X = int(input())
for i in range(X,10**6):
    if P[i]==1:
        print(i)
        break