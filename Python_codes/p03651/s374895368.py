from math import gcd
def main():
  n, k = map(int, input().split())
  a = list(map(int, input().split()))
  g = a[0]
  for i in range(1, n):
    g = gcd(g, a[i])
  if k <= max(a) and k % g == 0:
    print("POSSIBLE")
  else:
    print("IMPOSSIBLE")
if __name__ == "__main__":
  main()