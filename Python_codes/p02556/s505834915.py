n = int(input())

x_max = 0
y_max = 0
x_min = 10**9
y_min = 10**9

p_arr = [0]*n
m_arr = [0]*n

for i in range(n):
  x, y = map(int, input().split())
  p_arr[i] = x + y
  m_arr[i] = x - y
  

p_dist = max(p_arr) - min(p_arr)
m_dist = max(m_arr) - min(m_arr)
dist_max = max(p_dist, m_dist)
  
  
print(dist_max)