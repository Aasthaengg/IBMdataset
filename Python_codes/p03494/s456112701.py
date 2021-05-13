n = input()
nums = [int(i) for i in input().split(" ")]

def is_even(num_list):
  for num in num_list:
    if num % 2 != 0:
      return False
  return True

counter = 0
while(is_even(nums)):
  counter += 1
  nums = [n/2 for n in nums]
print(counter)
