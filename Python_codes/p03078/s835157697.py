#template
def inputlist(): return [int(k) for k in input().split()]
#template
X,Y,Z,K = inputlist()
A = inputlist()
B = inputlist()
C = inputlist()
li = []
for i in range(X):
    for j in range(Y):
        li.append(A[i]+B[j])
li.sort(reverse=True)
lis = []
lit=[]
for i in range(min(X*Y,K)):
    lis.append(li[i])
for i in range(min(X*Y,K)):
    for j in range(Z):
        lit.append(lis[i]+C[j])
lit.sort(reverse=True)
for i in range(K):
    print(lit[i])