# 0:a, b, c, a-b
# 1:b+c, a+c, a+b, b-a
# 2:2a+b+c, a+2b+c, a+b+2c, a-b
# 3:2a+3b+3c, 3a+2b+3c, 3a+3b+2c, b-a
# 4:6a+5b+5c, 5a+6b+5c, 5a+5b+6c, a-b
A, B, C, K = [int(x) for x in input().strip().split()]
ans = (A-B)*(-1)**(K%2)
if ans > 10 ** 18:
  print('Unfair')
else:
  print(ans)
