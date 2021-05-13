#自分が持っているクッキーの枚数が奇数なら、自分が持っているクッキーを 1 枚食べ、
#偶数なら何もしない。
#その後、自分が持っているクッキーの半分を相手に渡す。

a,b,k = [int(a) for a in input().split(' ')]

def cookie(p,q):
  if p%2==1:
    p -= 1
  p -= p/2
  q += p
  return (p,q)

for i in range(k):
  if i%2==0:
    # a turn
    a,b = cookie(a,b)
  else:
    # b turn
    b,a = cookie(b,a)
print( '{} {}'.format(int(a),int(b)) )