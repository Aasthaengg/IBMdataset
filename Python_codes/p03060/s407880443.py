n=int(input())
listv=list(map(int,input().split()))
listc=list(map(int,input().split()))
list=[]
for t in range(n):
  if listv[t]-listc[t]>0:
    list.append(listv[t]-listc[t])
print(sum(list))