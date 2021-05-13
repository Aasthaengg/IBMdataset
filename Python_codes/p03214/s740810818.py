N = int(input())
a_list = list(map(int, input().split()))

ave_a = sum(a_list) / N
flame_i = 0
dif_a = abs(a_list[0] - ave_a)

for i in range(1, N):
  if dif_a > abs(a_list[i] - ave_a):
    dif_a = abs(a_list[i] - ave_a)
    flame_i = i

print(flame_i)