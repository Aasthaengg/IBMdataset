n,m,l = input().split()

n = int(n)
m = int(m)
l = int(l)

matrix_A = [[0]*m for i in range(n)]
matrix_B = [[0]*l for j in range(m)]
matrix_C = [[0]*l for k in range(n)]
box_a = []
box_b = []
box_c = 0

for a in range(n):
    
    box_a = input().split()
    
    for b in range(m):
        
        matrix_A[a][b] = int(box_a[b])
        
    
for c in range(m):
    
    box_b = input().split()
    
    for d in range(l):
        
        matrix_B[c][d] = int(box_b[d])
        
            
for e in range(n):
    
    for f in range(l):
        
        for g in range(m):
            box_c += matrix_A[e][g] * matrix_B[g][f]
        
        
        matrix_C[e][f] = box_c
        box_c = 0
    
    print(" ".join(map(str,matrix_C[e])))
