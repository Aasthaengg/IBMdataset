A,B,C,D,E,F=map(int,input().split())
water=[]
suger=[]
for i in range(F//(100*A)+1):
    for j in range(F//(100*B)+1):
        if 0<100*(i*A+j*B)<=F:
            water.append(100*(i*A+j*B))
        if 100*(i*A+j*B)>F:
            break

for i in range((F*E//(100+E))//C+1):
    for j in range((F*E//(100+E))//D+1):
        if 0<=i*C+j*D<=F*E/(100+E):
            suger.append(i*C+j*D)
        if i*C+j*D>F*E/(100+E):
            break


c=0
w=100*A #初期値に注意！！！！！！
s=0
for i in range(len(water)):
    for j in range(len(suger)):
        if water[i]+suger[j]<=F and water[i]*E/100>=suger[j] and suger[j]/(water[i]+suger[j])>c:
            c=suger[j]/(water[i]+suger[j])
            w=water[i]
            s=suger[j]

print(w+s,s)
