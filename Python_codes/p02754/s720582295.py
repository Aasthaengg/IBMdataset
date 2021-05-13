N, A, B = map(int, input().split())


set_ = N // (A + B)
amari = N % (A + B)
if amari <= A:
  print(set_ * A + amari)
elif amari > A:
  print(set_ * A + A)