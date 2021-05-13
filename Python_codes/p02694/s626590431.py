## import math
X = int(input())
sum = 100
cnt = 0

while(sum < X):
  #sum += math.floor(sum*0.01)
  sum = sum*101//100
  cnt += 1

print(cnt)