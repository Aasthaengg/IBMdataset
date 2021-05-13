n = int(input())
l_v = [int(i) for i in input().split()]
l_c = [int(i) for i in input().split()]

t_v = []
t_c = []
for v, c in zip(l_v, l_c):
  if v > c:
    t_v.append(v)
    t_c.append(c)
    
print(sum(t_v) - sum(t_c))