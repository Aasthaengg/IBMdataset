kk = list(map(int, input().split()))
a = kk[0] - (kk[0] % kk[1])
b = a / kk[1]

if (kk[0] % kk[1]) == 0:
  answer = b * kk[2]
else:
  answer = (b + 1) * kk[2]
print(int(answer))