L=[]
ans="YES"
for i in range(3):
    a,b=map(int,input().split())
    L.append(a)
    L.append(b)
for i in range(1,5):
    if L.count(i)==3:
        ans="NO"
        break
print(ans)