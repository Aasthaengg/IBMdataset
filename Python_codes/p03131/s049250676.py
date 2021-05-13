K, A, B = (int(_) for _ in input().split())
ret = K + 1
if B - A - 2 > 0:
  c = max((K - A - 1)//2 + 1, 0)
  ret += c * (B - A - 2)
print(ret)