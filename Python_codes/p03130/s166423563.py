C=[0]*4
for _ in range(3):
    a,b=map(int,input().split())
    C[a-1]+=1
    C[b-1]+=1
print('YNEOS'[any(c>2 for c in C)::2])