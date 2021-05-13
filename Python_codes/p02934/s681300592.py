n = int(input())
a = list(map(int,input().split()))
sum_a_r = 0
def reciprocal(x):
  return 1 / x

for i in a:
  sum_a_r += reciprocal(i)
print(reciprocal(sum_a_r))