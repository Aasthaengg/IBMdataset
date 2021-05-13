lst=list(map(int,input().split()))
k=int(input())
for i in range(k):
  ind=lst.index(max(lst))
  lst[ind]*=2
print(sum(lst))