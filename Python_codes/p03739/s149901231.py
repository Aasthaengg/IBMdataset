n=int(input())
alist=list(map(int,input().split()))

cnt1=0
asum=0
#a0>0
for i in range(n):
  asum+=alist[i]
  if i%2==0:
    if asum<=0:
      cnt1+=1-asum
      asum+=1-asum
  else:
    if asum>=0:
      cnt1+=asum+1
      asum-=asum+1
      
cnt2=0
asum=0
#a0<0
for i in range(n):
  asum+=alist[i]
  if i%2==0:
    if asum>=0:
      cnt2+=asum+1
      asum-=asum+1
  else:
    if asum<=0:
      cnt2+=1-asum
      asum+=1-asum

#print(cnt1,cnt2)      
print(min(cnt1,cnt2))