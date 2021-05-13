import itertools
moji = str(input())
A,B,C,D = int(moji[0]),int(moji[1]),int(moji[2]),int(moji[3])

Bn = [B,B*-1]
Cn = [C,C*-1]
Dn = [D,D*-1]
flg = 0
for i,j,k in itertools.product(Bn, Cn,Dn):
    X = A + i + j + k
    if X == 7:
        break
    
print(str(A) + (str(i),"+"+str(i))[i >= 0]+ (str(j),"+"+str(j))[j >= 0]+ (str(k),"+"+str(k))[k >= 0]+"=7")    
