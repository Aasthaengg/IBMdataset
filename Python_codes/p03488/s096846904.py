import itertools
S=str(input())
x,y=map(int,input().split())
Move=[len(s) for s in S.split('T')]#偶数番目がｘ軸の移動量、奇数番目がy軸の移動量
x -=Move[0]#初手のみ正の方向
Move_x=Move[2::2]
Move_y=Move[1::2]

def check(d,x):
  se =set([0])
  for dx in d:
    se={a+b for a,b in itertools.product(se,[-dx,dx])}
  return (x in se)

print('Yes' if check(Move_x,x) and check(Move_y,y) else 'No')
