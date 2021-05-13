#D問題
K = int(input())

print(50)
align = [i for i in range(50)]
n = K//50
for i in range(50):
    align[i]+=n
    
L = K-50*n
for i in range(L):
    align[i]+=50
    for j in range(50):
        if i != j:
            align[j]-=1
            
print(*align)