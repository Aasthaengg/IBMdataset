N , M = list(map(int, input().split()))
broken = [1] * (N + 1)
for i in range(M):
  broken[int(input())] = 0
ANS = [0] * (N + 1)
ANS[0] = 1
ANS[1] = broken[1]
for i in range(N - 1):
  if(broken[i + 2]):
    if(broken[i + 1]): 
      ANS[i + 2] = (ANS[i + 1] + ANS[i]) %  (10 ** 9 + 7)
    else: 
      ANS[i + 2] = ANS[i] % (10 ** 9 + 7)
  else: ANS[i + 2] = 0
print(ANS[N])