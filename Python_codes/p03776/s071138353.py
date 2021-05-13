import math

nab = [int(x) for x in input().split()]
n = nab[0]
a = nab[1]
b = nab[2]
counts = []
nums = [int(x) for x in input().split()]
means = []
nums.sort(reverse = True)
for i in range(a, b+1):
  means.append(sum(nums[:i])/i)
  counts.append(int(math.factorial(nums.count(nums[i-1]))/(math.factorial(nums[:i].count(nums[i-1]))*math.factorial(nums.count(nums[i-1])-nums[:i].count(nums[i-1])))))

maxim = max(means)
print(maxim)
k = 0
count = 0
while k<len(means):
  if means[k]==maxim:
    count+=counts[k]
  k+=1
print(count)

#print(means.count(max(means)))

'''
def C(n, k):
  return C(n-1, k-1) + C(n-1, k)
  
for n in range(MAX_N):
  for k in range(MAX_K):
    C[n][k] = C[n-1][k-1] + C[n-1][k]
'''