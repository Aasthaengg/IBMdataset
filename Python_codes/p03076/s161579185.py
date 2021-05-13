N = [int(input()) for i in range(5)]
Ni = [0]*5
smallmin = 11
for i in range(5):
    Ni[i] = N[i]%10
    if Ni[i] == 0:
        Ni[i] = 10
    if Ni[i]<smallmin:
        smallmin = Ni[i]
        LAST = i
ans = 0
for i in range(5):
  if i == LAST:
    ans += N[i]
  else:
    ans = ans + N[i] + (10-Ni[i])
print(ans)
