N = int(input())
nums = list(map(int,input().split(" ")))
avr = sum(nums)/N
diff = 10 ** 9
ans = 0
for i,num in enumerate(nums):
  if diff > abs(avr - num):
    ans = i
    diff = abs(avr - num)
print(ans)