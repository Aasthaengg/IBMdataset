k,x = map(int,input().split())
l=[]
hidari=x-k+1
migi=x+k
if hidari< -(1000000):
    hidari= -(1000000)
if migi>1000000:
    migi=1000000
for i in range(hidari,migi):
    l.append(i)
lng=len(l)
print(" ".join(map(str,l)))