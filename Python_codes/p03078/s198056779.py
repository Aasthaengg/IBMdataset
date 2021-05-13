X,Y,Z,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

AB = []
for a in A:
    for b in B:
            AB.append(a+b)
AB = sorted(AB,reverse=True)[:K]
C = sorted(C,reverse=True)
ABC = []

for c in C:
    for ab in AB:
        ABC.append(c + ab)
ABC = sorted(ABC,reverse=True)        
print(*ABC[:K],sep="\n")        
    
