n = int(input())
tn = [0]+[int(i) for i in input().split()]+[0]
an = [0]+[int(i) for i in input().split()]+[0]
ans = 1
mod = 10**9+7

for i in range(1,n+1):
  if tn[i-1] < tn[i] and an[i] > an[i+1]:
    ans *= int(tn[i] == an[i])
  elif tn[i-1] < tn[i] and an[i] == an[i+1]:
    ans *= int(tn[i] <= an[i])
  elif tn[i-1] == tn[i] and an[i] > an[i+1]:
    ans *= int(tn[i] >= an[i])
  else:
    ans *= min(an[i],tn[i])
    ans %= mod
print(ans)