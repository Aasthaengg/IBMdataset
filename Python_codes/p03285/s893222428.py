n=int(input())
f=0
for i in range(30):
    for j in range(30):
        if 4*i+7*j==n:
            f=1
print("Yes" if f==1 else "No")
        
    
