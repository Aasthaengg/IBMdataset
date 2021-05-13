n = int(input())
def func(x):
  answer = list(map(int,str(x)))
  return sum(answer)
nums = []
for a in range(1,n):
  b = n - a
  num = func(a) + func(b)
  nums.append(num)
print(min(nums))