N = int(input())
T = list(map(lambda t: int(t), input().split(" ")))
M = int(input())
P = []
T_new = []
T_diff = []
for i in range(M):
  tmp = input().split(" ")
  P.append(int(tmp[0]) - 1)
  T_new.append(int(tmp[1]))
  T_diff.append(T_new[i] - T[P[i]])

T_sum = sum(T)
print("\n".join([str(T_sum + t_d) for t_d in T_diff]))