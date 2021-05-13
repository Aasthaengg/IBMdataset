N = int(input())
A = list(map(int,input().split()))
A.sort()
final_list = []
plus = sum(x >= 0 for x in A)

def pop(length, flag):
  val = A[flag]
  A.pop(flag)
  for i in range(length):
    next_add = A[-1 - flag]
    final_list.append((val, next_add))
    val = val - next_add
    A.pop(-1 - flag)
  return val

if plus == N: #全部正の数
  ans = pop(N - 2, 0)
  final_list.append((max(ans, A[0]), min(ans, A[0])))
  ans = abs(ans - A[0])
elif plus == 0: #全部負の数
  ans = pop(N - 2, -1)
  final_list.append((max(ans, A[0]), min(ans, A[0])))
  ans = abs(ans - A[0])
else:
  ans_neg = pop(plus - 1, 0)
  ans_pos = pop(N - plus - 1, -1)
  final_list.append((ans_pos, ans_neg))
  ans = ans_pos - ans_neg
  


print(ans)
for i in range(len(final_list)):
  print(final_list[i][0], " ", final_list[i][1])