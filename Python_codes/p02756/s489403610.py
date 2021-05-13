s = input()
n = int(input())
c = 0
left_l = ['', '']
right_l = ['', '']
s_l = [s, s[::-1]]
for _ in range(n):
  lst = [i for i in input().split()]
  if lst[0] == '1':
    if c == 1:
      s_l[0], s_l[1] = s_l[1], s_l[0]
      #print(s)
    else:
      s_l = [right_l[1] + s_l[1] + left_l[1], left_l[0] + s_l[0] + right_l[0]]
      left_l[0], left_l[1] = '', ''
      right_l[0], right_l[1] = '', ''
      c = 1
      #print(s)
  elif lst[0] == '2':
    c = 0
    if lst[1] == '1':
      left_l[0] = lst[2] + left_l[0]
      left_l[1] = left_l[1] + lst[2]
    elif lst[1] == '2':
      right_l[0] = right_l[0] + lst[2]
      right_l[1] = lst[2] + right_l[1]
w = left_l[0] + s_l[0] + right_l[0]
print(w)
