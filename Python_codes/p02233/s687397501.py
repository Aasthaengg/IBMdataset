n = int(input())
f = [1,1]
for i in range(2,n+1):
    nf = f[i-2] + f[i-1]
    f.append(nf)
    
    
print(f[n])
