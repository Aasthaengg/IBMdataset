n = int(input())
t, a = map(int, input().split())
heights = [int(x) for x in input().split()]

result = -1
min_value = 10 ** 9
for i, h in enumerate(heights):
  temp = abs(a - (t - h * 0.006))
  if temp < min_value:
    result = i + 1
    min_value = temp
    
print(result) 