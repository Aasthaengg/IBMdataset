TAB = [list(map(int, input().split())) for _ in range(3)]
T = TAB[0]
A = TAB[1]
B = TAB[2]
dV1, dV2 = A[0] - B[0], A[1] - B[1]

dL1, dL2 = dV1 * T[0], dV2 * T[1]
if dL1 + dL2 == 0:
  print("infinity")
else:
  if dL1 * (dL1 + dL2) > 0:
    print(0)
  else:
    m = dL2 * T[0] - dL1 * T[1]
    n = dL1 + dL2
    m += n * T[1]
    cnt = m // (n * (T[0] + T[1]))
    if m % (n * (T[0] + T[1])) == 0:
      print(2*cnt-2)
    else:
      print(2*cnt-1)