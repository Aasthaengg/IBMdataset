A, B = map(int, input().split())

mark = ['.', '#']

def print_ans(ans):
  for a in ans:
    print(''.join(a))

def change(num, mark_id):
  global ans
  idx = 0
  while num > 1:
    if idx <= 99:
      ans[-1][idx] = mark[mark_id]
      idx += 2
      num -= 1
    else:
      ans.extend([list(mark[mark_id-1]*100) for i in range(2)])
      idx = 0

  
ans = [list(mark[0] * 100)]
change(B, 1)
ans.append(list(mark[0] * 100))
ans.extend([list(mark[1]*100) for i in range(2)])
change(A, 0)

print(len(ans), 100)
print_ans(ans)