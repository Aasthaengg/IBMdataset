n = int(input())
X = list(map(int,input().split()))
Y = list(map(int,input().split()))
P = []
P_1 = 0
P_2 = 0
P_3 = 0
P_m = 0

for i in range(n):
    if X[i] > Y[i]:
        P.append(X[i]-Y[i])
    else:
        P.append(Y[i]-X[i])

for i in range(n):
    P_1 += P[i]
    P_2 += P[i]**2
    P_3 += P[i]**3
P_2 = P_2**(1/2)
P_3 = P_3**(1/3)
P_m = max(abs(x-y) for x,y in zip(X,Y))

print('{:.6f}'.format(P_1))
print('{:.6f}'.format(P_2))
print('{:.6f}'.format(P_3))
print('{:.6f}'.format(P_m))
