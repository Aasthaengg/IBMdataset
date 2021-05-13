n = int(input())
a = input()
b = input()
c = input()

ans = 0
for aa, bb, cc in zip(a,b,c):
  if aa == bb and bb == cc:
    pass
  elif aa == bb or bb == cc or cc == aa :
    ans += 1
  else :
    ans += 2
print(ans)

