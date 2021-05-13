#１回目の操作で最低5点、2回目以降は6点と5点を繰り返す
x = int(input())
#print(x,'/',11,x//11,x%11)
#print(x,'/',5,x//5,x%5)

tmp1 = x//11
tmp2 = (x%11)//6
tmp3 = (x%11)%6
if tmp3 > 0:
    print(tmp1*2+tmp2+1)
else:
    print(tmp1*2+tmp2)
