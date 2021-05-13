N,K = map(int,input().split())
cc = list(map(int,input().split()))
dice_sum = sum(cc[:K])
max_dice = dice_sum
for i in range(N-K):
  dice_sum = dice_sum + cc[i+K] - cc[i]
  max_dice = max(max_dice,dice_sum)
print((max_dice+K)/2)