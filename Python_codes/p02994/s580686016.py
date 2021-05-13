n,k=map(int,input().split());a=[k+i for i in range(n)]
sumA=sum(a);min_num=float('inf');result=0
for i in a:
  if min_num > abs(sumA-(sumA-i)):
    min_num=abs(sumA-(sumA-i))
    result=sumA-i
print(result)