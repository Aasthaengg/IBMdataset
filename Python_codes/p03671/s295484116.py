import itertools
def main():
  s = list(map(int,input().split()))
 # m = itertools.combinations(s,2)
  ans = float("inf")
#  print(m)
  for m in itertools.combinations(s,2):
    ans = min(ans,sum(m))
  print(ans)
if __name__ == '__main__':
  main()