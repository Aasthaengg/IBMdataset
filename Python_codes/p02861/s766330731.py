N = int(input())
xs, ys = [], []
for n in range(N):
  x, y = map(int, input().split(' '))
  xs.append(x)
  ys.append(y)
  
sum_dist = 0
for n1 in range(N-1):
  for n2 in range(n1+1, N):
    sum_dist += ((xs[n1]-xs[n2])**2 + (ys[n1]-ys[n2])**2)**(1/2)

# 辺abを通る組み合わせ数は，頂点a,bをセットと見た順列なので，2!(n-1)!．
# グラフは対称で全ての辺を同じ回数通るので，組み合わせの平均を考えると，
# ave_dist = 2!(n-1)!*sum_dist / n! = 2*sum_dist / n
print((2 * sum_dist) / N)