# AGC032 Problem-B

n = int(input())

table =  [[ 1 for i in range(0, n)] for j in range (0,n)]

#print (table)

if n % 2 == 1 : # odd
    m = n-2
else :
    m = n-1

for i in range (0, n) : 
    table[i][m-i] = 0
#print (table)

print (n*(n-1)//2 - n//2 )
for i in range (0,n):
    for j in range (0,i):
        if table[i][j] ==1 :
            print (i+1, j+1)


