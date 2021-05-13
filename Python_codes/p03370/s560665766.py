n,x =map(int, input().split())

m_list = []
for i in range(n):
  m_list.append(int(input()))
m_list = sorted(m_list)
remain_x = x - sum(m_list)

cnt_list = []
for i in m_list:
  if remain_x >= i:
    cnt = remain_x // i
    cnt_list.append(cnt)
    remain_x = remain_x % (i *cnt)
  else:
    break

print(n + sum(cnt_list))