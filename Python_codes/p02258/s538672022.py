n = input()
maxi = -1 * 10**9
mini = input()


for i in range(n-1):
  tmp = input()
  maxi = max(maxi, tmp - mini)
  mini = min(mini, tmp)

print maxi