n = int(input())
heights = list(map(int, input().split()))

ans_list = [0]*n
for i in range(n):
  if i == 0:
    continue
  else:
    if heights[i] <= heights[i-1]:
      ans_list[i] = ans_list[i-1]+1
    else:
      ans_list[i] = 0
      
ans_list.sort()
ans = ans_list[-1]
print(ans)