A = int(input())
B = int(input())
C = int(input())
X = int(input())

suma = 0
sumb = 0
sumc = 0

la = list([0])
lb = list([0])
lc = list([0])

ls = list()
for i in range(1,A+1):
    suma = suma + 500
    la.append(suma)

for i in range(1,B+1):
    sumb = sumb + 100
    lb.append(sumb)

for i in range(1,C+1):
    sumc = sumc + 50
    lc.append(sumc)

for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            ls.append(la[i]+lb[j]+lc[k])
            
print(ls.count(X))