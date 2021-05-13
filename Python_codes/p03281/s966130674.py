n = int(input())
m = 0
k=0

for i in range(1,n+1,2):
    k =0
    for j in range(1,i+1):
        if i % j == 0:
            k = k+1  
        if k == 8:
            m = m +1

print(m)