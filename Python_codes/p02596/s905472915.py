#数列が与えられたら漸化式を作る
#a1 = 7, ai = 10 * a(i - 1) + 7 (i >= 2)
K = int(input())
a = [7 % K] #a1 mod K
for i in range(K - 1): #a2 - aK
  a.append((10 * a[i] + 7) % K) #mod K
for i in range(K):
  if a[i] == 0:
    print(i + 1)
    break
else: print(-1)