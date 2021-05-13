# coding: utf-8
# Your code here!
N,T=map(int,input().split())
A=list(map(int,input().split()))

buy=10**9
buy_loc=[]
benefit=0
for index,item in enumerate(A):
    if buy>item:
        buy=item
        buy_loc.append(index)
    benefit=max(item-buy,benefit)

buy_loc.append(10**6)
buy_loc=buy_loc[::-1]

ans=0
buy_count=0
sell_count=0
for i in range(len(A)):
    if i==buy_loc[-1]:
        buy_loc.pop(-1)
        buy=A[i]
        #print(buy_count,sell_count)
        ans+=min(buy_count,sell_count)
        buy_count=0
        sell_count=0
    if A[i]==buy:
        buy_count+=1
    if A[i]-buy==benefit:
        sell_count+=1

ans+=min(buy_count,sell_count)
print(ans)
#print(benefit)
#print(buy_loc)