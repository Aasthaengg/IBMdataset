N = int(input())
a = list(map(int, input().split()))
score_A = 0
score_B = 0
a.sort(reverse=True)
i = 1
for n in a:
  if i % 2 == 1:
    score_A += n
  elif i % 2 == 0:
    score_B += n
  
  i += 1


result = score_A - score_B
print(result)