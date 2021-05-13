S = input()
T = input()

min_m = len(T)
dif = range(len(S)-min_m+1)

for j in dif:
  St = S[j:len(T)+j]
  miss = 0
  for i in range(len(T)):
    if St[i] != T[i]:
      miss += 1
  if miss < min_m:
    min_m = miss

print(min_m)
