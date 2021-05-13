N = int(input())
Alist = list(map(int,input().split()))

anslist = [0]*(N+1)
for i in range(len(Alist)):
  anslist[Alist[i]]+=1
#print (anslist)
for i in range(len(anslist)):
  if i!=0:
    print (anslist[i]) 