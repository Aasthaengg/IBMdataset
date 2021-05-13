n, a, b = map(int, input().split())

num_lists = list(range(1, n+1, 1))
sum_lists = []
for i in num_lists:
  count = 0
  j = i
  while j >0:
    ans = j%10
    count += ans
    j = j//10
  if a <= count and count <= b:
    sum_lists.append(i)

answer = 0
for i in sum_lists:
  answer += i

print(answer)