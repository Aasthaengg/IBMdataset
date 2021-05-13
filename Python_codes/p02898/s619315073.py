def inp():return map(int,input().split())
def linp():return list(map(int,input().split()))

s=0
n,k=inp()
l=linp()
for x in l:
    if x>=k:s+=1
print(s)

