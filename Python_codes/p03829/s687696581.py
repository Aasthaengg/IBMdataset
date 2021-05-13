N, A, B = map(int, input().split())
towns = list(map(int ,input().split()))
sum_e = 0
for i in range(1, N):
  dis = towns[i] - towns[i-1]
  if dis * A > B:
    sum_e += B
  else:
    sum_e += dis * A
print(sum_e)