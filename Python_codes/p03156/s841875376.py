n = int(input())
a, b = map(int, input().split())
p = list(map(int, input().split()))
prob_1 = 0
prob_2 = 0
prob_3 = 0
for i in range(n):
  if p[i] <= a:
    prob_1 += 1
  elif p[i] <= b:
    prob_2 += 1
  else:
    prob_3 += 1
ans = min(prob_1, prob_2, prob_3)
print(ans)