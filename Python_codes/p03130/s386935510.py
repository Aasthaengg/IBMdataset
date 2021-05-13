a1,b1=input().split()
a2,b2=input().split()
a3,b3=input().split()
lista=[a1,a2,a3,b1,b2,b3]
yn=0
for i in range(1,5):
    if lista.count(str(i))==0 or lista.count(str(i))>2:
        yn=1
        break
if yn==1:
    print("NO")
else:
    print("YES")
