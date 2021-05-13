N = int(input())
ratios = [[i for i in map(int,input().split())] for j in range(N)]

ans_a = 0
ans_t = 0
ratio = ratios.pop(0)
ans_a = ratio[0]
ans_t = ratio[1]

for ratio in ratios:
  i = max(ans_a // ratio[0], ans_t // ratio[1])
  while True:
    temp_a = ratio[0]*i
    temp_t = ratio[1]*i
    if temp_a >= ans_a and temp_t >= ans_t:
      ans_a = temp_a
      ans_t = temp_t
      break
    i += 1
    
print(ans_a + ans_t)