n=int(input())
li=[]
res = 1
for i in range(n):
    li += [input()]
la=sorted(li)
for i in range(1,n):
    if la[i-1]!=la[i]:res += 1
print(res)