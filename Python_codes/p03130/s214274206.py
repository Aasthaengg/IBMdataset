t=[0]*4
for i in range(3):
    a,b=map(int,input().split())
    t[a-1]+=1
    t[b-1]+=1
print('YES' if max(t)<3 else 'NO')