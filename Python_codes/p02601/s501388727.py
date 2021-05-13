import random

nums = input().split()

#print(nums)
#A = nums[0]
#B = nums[1]
#C = nums[2]
a = int(nums[0])
b = int(nums[1])
c = int(nums[2])
#print(a)
K = input()
k = int(K)

#print(type(a))

#print(k)

cnt = 0

#print(type(cnt))

while a >= b:
  cnt +=1
  b *= 2
  #print(b)

while b >= c:
  cnt += 1
  c *= 2
  #print(c)
  
#if cnt

  
if cnt <= k:
  print("Yes")
else:
  print("No")

	

#for hoge in range(1,k +1):
#	print(hoge)
#print(random.choice(nums))

#print(A)