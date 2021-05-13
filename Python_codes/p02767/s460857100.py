N = int(input())
X = list(map(int, input().split()))

ave = sum(X) / float(N)
my_round_int = lambda x: int((x * 2 + 1) // 2)
t = my_round_int(ave)
val = 0
for x in X:
  val += (t - x)**2
print(val)
