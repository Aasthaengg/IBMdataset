def main():
  N = int(input())
  A = [int(_) for _ in input().split()]
  k = f = 0
  can = False
  for a in A:
    if a%2 == 1:
      k += 1
    if a%4 == 0:
      f += 1
  if k == 0: #すべて偶数の場合
    can = True
  else:
    if N - k - f == 0:
      if f+1 >= k:
        can = True
    else:
      if f >= k:
        can = True
  print('Yes' if can else 'No')
  return

if __name__ == '__main__':
  main()