N=int(input())
X=[]

for i in range(1,N+1):
    S,P=input().split()
    X.append((S,-int(P),i))

X.sort()
for (_,_,c) in X:
    print(c)
