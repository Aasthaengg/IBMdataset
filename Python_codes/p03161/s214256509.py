N, K = map(int, input().rstrip().split(' '))
frog_lst = list(map(int, input().rstrip().split(' ')))
frog_jump_lst = []

def frog_jump(frog_jump_lst=[], index=0):
  if not frog_jump_lst:
    frog_jump_lst.append(0)
  else:
    now_pos = frog_lst[index]
    k = min(K, len(frog_jump_lst))
    pattern = [abs(now_pos - frog_lst[index-i]) + frog_jump_lst[-i] for i in range(1,k+1)]
    frog_jump_lst.append(min(pattern))

for j in range(N):
  frog_jump(frog_jump_lst, j)
print(frog_jump_lst[-1])