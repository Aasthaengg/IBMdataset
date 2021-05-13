n,k =map(int,input().split())
amountList=list(map(int,input().split()))
amountList.sort()
sum =0
for num in range(k):
  sum += amountList[num]

print(sum)
