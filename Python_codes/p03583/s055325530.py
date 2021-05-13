N = int(input())

# a >= b >= c を仮定できる
# a,b,c <= 3500
# 4/N <= 3/a  a <= 0.75N
# 4/N >= 3/c  c >= 0.75N

least = int(0.75 * N) + 2
max = 3501
for b in range(1,max):
  for a in range(1,least):
    res = 4/N - 1/a - 1/b
    if res<=0:
      continue
    candc = int(1/res)
    for c in range(candc-1,candc+2):
      if 4*a*b*c == N*(a*b + b*c + c*a):
        print(a,b,c)
        exit(0)

