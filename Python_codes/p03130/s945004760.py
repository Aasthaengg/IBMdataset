p=[0]*4

for i in range(3):
    a,b=map(int,input().split())
    p[a-1]+=1
    p[b-1]+=1
    
odd=0
for i in range(4):
    if p[i]%2==1:
        odd+=1
        
if odd<=2:
    print("YES")
else:
    print("NO")