a,b,c = map(int,input().split())
count = 0
if a!=b and a!=c: 
    if b!=c: 
        count = 3
    elif b==c: 
        count = 2
else:
    if a==b or a==c:
        count+=1
    if b!=c:
        count+=1
print(count)