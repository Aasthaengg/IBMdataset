from collections import defaultdict
n= int(input())
D=list(map(int,input().split()))

m=int(input())
T=list(map(int,input().split()))

dicta=defaultdict(lambda:0)
dictb=defaultdict(lambda:0)

for i in range(n):
    dicta[D[i]]+=1

for i in range(m):
    dictb[T[i]]+=1


ans="YES"
for i in range(m):
    if dicta[T[i]]<dictb[T[i]]:
        ans="NO"
        break

print(ans)
