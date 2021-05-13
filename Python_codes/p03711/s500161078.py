x,y=map(int,input().split())
count=0
l=[1,3,5,7,8,10,12]
r=[4,6,9,11]
result='No'
for i in l:
    if i==x or i==y:
        count+=1
if count==2:
    result='Yes'
count=0
for c in r:
    if c==x or c==y:
        count+=1
if count==2:
    result='Yes'
print(result)