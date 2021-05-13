N = int(input())
m = 10000000
def judge_1(t):
  c = 0
  while t>0:
    c += t%6
    t = t//6  
  return c
def judge_2(t):
  c = 0
  while t>0:
    c += t%9
    t = t//9  
  return c
for i in range(N+1):
  m = min(m, judge_1(i)+judge_2(N-i))
print(m)