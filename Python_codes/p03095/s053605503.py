n=int(input())
s=input()
# 数値(1〜26)→アルファベット(a〜z)
n2a = lambda c: chr(c+64).lower()
al=[]
for i in range(1,27):
  c=s.count(n2a(i))
  if c!=0:
    al.append(c)
def func(nums):
  if len(nums)==1:
    return nums[0]%(10**9+7)
  elif len(nums)==2:
    return (nums[0]+nums[1]+nums[0]*nums[1])%(10**9+7)
  else:
    num=func(nums[1:])
    return (nums[0]+num+nums[0]*num)%(10**9+7)
print(func(al))

