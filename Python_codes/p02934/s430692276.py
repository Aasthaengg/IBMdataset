n=int(input())
l=list(map(int,input().split()))
sum=0
for ll in l:
  sum+=1/ll
print(1/sum)