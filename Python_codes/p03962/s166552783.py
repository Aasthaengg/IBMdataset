a=input().split()
a.sort()
cnt=0
while len(a)>0:
    i=a.count(a.pop(0))
    for j in range(i):
        a.pop(0)
    cnt+=1
print(cnt)