n=int(input())
l=[]
tmp=0
i=1
while tmp<n:
    tmp+=i
    l.append(i)
    i+=1
k=tmp-n
if k>0:
    l.remove(k)
for item in l:
    print(item)