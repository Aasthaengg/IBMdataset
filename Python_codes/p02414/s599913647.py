n,m,l = map(int,input().split())
A=[]
B=[]
for i in range(n): A.append(list(map(int,input().split())))
for j in range(m): B.append(list(map(int,input().split())))
for A_r in A:
    print(" ".join(map(str,[sum([x*y for x,y in zip(A_r,[B_r[k] for B_r in B])]) for k in range(l)])))
