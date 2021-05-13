S = input()
T = input()
l = len(S)
m = len(T)

for n in range(l-m+1):
  if all(c in "?"+d for c,d in zip(S[-n-m:],T)):
    S = S.replace("?","a")
    print(S[:-n-m]+T+S[l-n:])
    exit()

print("UNRESTORABLE")