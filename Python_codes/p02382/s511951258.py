# coding: utf-8
#72

n = int(input())
X = list(map(int,input().split()))
Y = list(map(int,input().split()))
#print(X,Y)

D=[]
for j in range(n):
    d=abs(X[j]-Y[j])
    D.append(d)
print('{:.05f}'.format(sum(D)))

E=[]
for i in range(n):
    e=D[i]**2
    E.append(e)
A=sum(E)**(1/2)
print('{:.05f}'.format(A))

F=[]
for i in range(n):
    f=D[i]**3
    F.append(f)
B=sum(F)**(1/3)
print('{:.05f}'.format(B))

print('{:.05f}'.format(max(D)))


