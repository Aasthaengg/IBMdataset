
SOSU = (10**9 + 7)

n, k = list(map(int, input().split(' ')))
A = list(map(int, input().split(' ')))

#print(A)

cntall = 0
cntusiro = 0

for indexi, i in enumerate(A):
    for indexj, j in enumerate(A):
        if i > j :
            cntall += 1
            if indexi < indexj:
                cntusiro += 1
        #print("roop:",i,j,indexi,indexj,cntall,cntusiro)

anst = (k*(k -1))*cntall//2 + k * cntusiro 


ans = anst % SOSU

#print ( cntall, cntusiro)
#print(anst)
print(int(ans) )