def main():
  A, B = map(int,input().split())
  i1 = max(A * 12.5, B * 10.0)
  i2 = min((A + 1) * 12.5, (B + 1) * 10.0)
  i = int(i1)
  while i < i2:
    if i >= i1: return i
    i += 1
  return -1

ans = main()
print(ans)