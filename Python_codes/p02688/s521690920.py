n,k=map(int,input().split())
data=[] 
for i in range(n): 
    data.append(i+1)

for i in range(k): 
    d=int(input()) 
    a=list(map(int,input().split())) 
    for j in range(d): 
        if a[j] in data: 
            data.remove(a[j]) 
        else: 
            pass 
print(len(data))