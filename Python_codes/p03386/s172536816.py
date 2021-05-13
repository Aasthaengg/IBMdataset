ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

a,b,k=nm()
nums=set()
for i in range(a,min(a+k,b)):
  nums.add(i)
for i in range(max(a,b-k+1),b+1):
  nums.add(i)

for n in sorted(nums):
  print(n)
