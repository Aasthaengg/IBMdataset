import itertools
# x, y方向独立
# 初手のみ正なことに注意

txt = input()
x,y = map(int,input().split())
d = [len(s) for s in txt.split('T')]
x -= d[0]

d_x = d[2::2]
d_y = d[1::2]

def check(d,x):
  se = set([0])
  for dx in d:
    se = {a+b for a,b in itertools.product(se,[-dx,dx])}
  return (x in se)

bl = check(d_x,x) and check(d_y,y)
print('Yes' if bl else 'No')