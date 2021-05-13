n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))


u = set()

def agari(i):
    if X[i]==1:
        X[i]=0
        agari(i+1)
    else:
        X[i]=1

X = [0]*20
k=0
while k<(pow(2,n)-1):
    y = 0
    for l in range(n):
        y += A[l]*X[l]
    u.add(y)
    agari(0)
    k+=1

for j in range(q):
    if m[j] in u:
        print("yes")
    else:
        print("no")
