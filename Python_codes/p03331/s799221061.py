N = int(input())
list_candi = []
for A in range(1, N):
  B = N - A
  list_A = list(map(int, list(str(A))))
  list_B = list(map(int, list(str(B))))
  sum_list= sum(list_A) + sum(list_B)
  list_candi.append(sum_list)
print(min(list_candi))