
n = int(input())

a = list(map(int,input().split()))

b1 = []

b2 = []

for i in range(0,len(a),2):
    b1.append(a[i])
    
for i in range(1,len(a),2):
    b2.append(a[i])
    
if n%2 == 0:
    b2.reverse()
    b2.extend(b1)
    for i in b2:
        print(i,end = " ")
        
else:
    b1.reverse()
    b1.extend(b2)
    for i in b1:
        print(i,end = " ")