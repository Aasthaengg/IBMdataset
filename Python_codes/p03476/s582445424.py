import bisect

sosu=set()
nums=[1]*(10**5+1)
for i in range(2, 10**5+1):
  if nums[i]==1:
    sosu.add(i)
    j=i
    while j<10**5+1:
      nums[j]=0
      j+=i
      
nums=[x for x in range(3, 2*10**5+1, 2) if x in sosu and (x+1)//2 in sosu]

Q=int(input())
for _ in range(Q):
  l, r=map(int, input().split())
  a=bisect.bisect_left(nums, l)
  b=bisect.bisect_right(nums, r+1)
  print(b-a)