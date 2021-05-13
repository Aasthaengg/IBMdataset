N = int(input())
nums = list(map(int, input().split()))
even_cnt = 0
for num in nums:
  if num%2 == 0:
    even_cnt += 1
print(3**N-2**even_cnt)