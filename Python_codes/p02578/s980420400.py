n = int(input())
a = list(map(int, input().split()))
max_a_list = [0]*n
max_a_list[0] = a[0]

for i in range(1,n):
  max_a_list[i] = max(max_a_list[i - 1],a[i])
sum_ = 0
for i in range(n):
  if max_a_list[i] > a[i]:
    sum_ += max_a_list[i] - a[i]
print(sum_)

