ABCDE = [int(input()) for _ in range(5)]
k = int(input())

ans = 0
for i in range(4):
  for j in range(i + 1, 5):
    ans += int(abs(ABCDE[i] - ABCDE[j]) > k)
    
if ans > 0:
  print(":(")
else:
  print("Yay!")