N,K,C=map(int,input().split())
S=list(input())

work_last=-float("inf")
llist=[]
for i in range(1,N+1):
  if S[i-1]=="o":
    if i-work_last>C:
      llist.append(i)
      work_last=i
  if len(llist)==K:
    break
#print(llist)

work_last=float("inf")
rlist=[]
for i in reversed(range(1,N+1)):
  if S[i-1]=="o":
    if work_last-i>C:
      rlist.append(i)
      work_last=i
  if len(rlist)==K:
    break
rlist.reverse()
#print(rlist)

for i in range(K):
  if llist[i]==rlist[i]:
    print(llist[i])