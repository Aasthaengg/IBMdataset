def main():
  n = int(input())
  hs = tuple(map(int, input().split()))
 
  a, b = 0, abs(hs[1] - hs[0])
 
  for i in range(2, n):
    c = hs[i]
    d1 = a + abs(c - hs[i-2])
    d2 = b + abs(c - hs[i-1])
    a, b = b, d1 if d1 <= d2 else d2
 
  print(b)
 
if __name__ == "__main__":
  main()