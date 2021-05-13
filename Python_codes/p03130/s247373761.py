l=[]
for i in range(3):
    l.extend(list(map(int,input().split())))
m=[0,0,0,0]
for i in range(1,5):
    m[i-1]=l.count(i)
if sorted(m) == [1,1,2,2]:
    print("YES")
else:
    print("NO")