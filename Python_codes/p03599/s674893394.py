import itertools
def main():
  A, B, C, D, E, F = map(int, input().split())
  water = [100*A*(i)+100*B*(j) for i in range(31) for j in range(31-i)]
  water = set(water)
  sugar_max = int(F*(E/(100+E)))
  sugar = [C*i + D*j for i in range(sugar_max//C+10) for j in range((sugar_max-C*i)//D+10)]
  sugar = set(sugar)
  ans = [0, 0]
  max_den = 0
  for p in itertools.product(water, sugar):
    if p[0] == 0 and p[1] == 0:continue
    if max_den <= p[1]/(p[0]+p[1]) <= E/(100+E) and p[0] + p[1] <= F:
      max_den = p[1]/(p[0]+p[1])
      ans[0] = p[0] + p[1]
      ans[1] = p[1]
  print(*ans)
if __name__ == "__main__":
  main()
